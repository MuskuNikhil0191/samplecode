const exp=require('express');
const app=exp();
const request=require('request');
const errorhandler=require('express-async-handler');
const cors=require('cors');
const dburl="mongodb+srv://nick:nick@cluster0.h4wuj.mongodb.net/placementsinfo?retryWrites=true&w=majority";
const mc=require('mongodb').MongoClient;
const { ReplSet } = require('mongodb');
let dcolobj;
let ucolobj;
let ccolobj;
mc.connect(dburl,{useNewUrlParser:true,useUnifiedTopology:true})
.then(client=>{
    const dbobj=client.db("placementsinfo");
    dcolobj=dbobj.collection("data");
    ucolobj=dbobj.collection("users");
    ccolobj=dbobj.collection("students");
    console.log("db connection success");
})
.catch(err=>{console.log("error in db connection",err)});
app.use(exp.json());
app.use(cors({origin:"http://localhost:4200"}));

//users api calls
app.get('/getuser/:rollno/:pwd',errorhandler(async(req,res,next)=>{
    let userrollno=req.params.rollno;
    userrollno=userrollno.toUpperCase();
    let userpwd=req.params.pwd;
    let exrollno=await ucolobj.findOne({rollno:userrollno});
    let expwd=await ucolobj.findOne({$and:[{rollno:userrollno},{password:userpwd}]});
    if(exrollno!=null && expwd!=null){
        res.json({message:"success",data:expwd});
    }
    else if(exrollno==null){
        res.json({message:"invalidrollno"});
    }
    else{
        res.json({message:"invalidpwd"});
    }
}))
app.post('/createuser',errorhandler(async (req,res,next)=>{
    let user=req.body;
    user.rollno=user.rollno.toUpperCase();
    user.email=user.email.toLowerCase();
    let userrollno=user.rollno;
    let userclg=user.college;
    let usermail=user.email;
    request.get(`http://localhost:4000/getrollno/${userrollno}/${userclg}`,errorhandler(async(error,response,body)=>{
        if(error){
            return console.log(error);
        }
        if(body=="invalidrollno"){
            return res.json("invalidrollno");
        }
        else{
            let existrollno=await ucolobj.findOne({rollno:userrollno});
            let exmail=await ucolobj.findOne({email:usermail});
            if(existrollno!=null){
                return res.json("existingrollno");
            }
            else if(exmail==null){
                await ucolobj.insertOne(user);
                return res.json(user);
            }
            else{
                return res.json("existingemail");
            }
        }
    }))
}))
app.put('/updatepwd',errorhandler(async (req,res,next)=>{
    let userpwd=req.body.password;
    let usermail=req.body.email;
    usermail=usermail.toLowerCase();
    let exuser=await ucolobj.findOne({email:usermail});
    if(exuser==null){
        res.json("invalidemail");
    }
    else{
        await ucolobj.updateOne({email:usermail},{$set:{password:userpwd}});
        res.json("Successfully updated Password!");
    }
}))
app.delete('/deleteuser/:rollno',errorhandler(async (req,res,next)=>{
    let userrollno=req.params.rollno;
    userrollno=userrollno.toUpperCase();
    await ucolobj.deleteOne({rollno:userrollno});
    res.json("success");
}))

//data apicalls
app.get('/getdata',errorhandler(async (req,res,next)=>{
    let users=await dcolobj.find().toArray();
    res.send(users);
}))
app.post('/enterdata',errorhandler(async (req,res,next)=>{
    let user=req.body;
    await dcolobj.insertOne(user);
    res.json("success");
}))
app.delete('/deletedata/:rollno',errorhandler(async(req,res,next)=>{
    let userrollno=req.params.rollno;
    console.log(userrollno)
    // userrollno=userrollno.toUpperCase();
    let msg=await dcolobj.deleteOne({_id:userrollno});
    res.json({message:"success",response:msg});
}))
//college api calls
app.post('/enterrollno',errorhandler(async(req,res,next)=>{
    let user=req.body;
    user.rollno=user.rollno.toUpperCase();
    await ccolobj.insertOne(user);
    res.json("success");
}))
app.get('/getrollno/:rollno/:clg',errorhandler(async(req,res,next)=>{
    let userrollno=req.params.rollno;
    userrollno=userrollno.toUpperCase();
    let userclg=req.params.clg;
    let exuser=await ccolobj.findOne({$and:[{rollno:userrollno},{college:userclg}]});
    if(exuser!=null){
        res.send("success");
    }
    else{
        res.send("invalidrollno");
    }
}))
app.get('/getrollnos',errorhandler(async(req,res,next)=>{
    let users=await ccolobj.find().toArray();
    res.json(users);
}))
app.delete('/deleterollno/:rollno',errorhandler(async(req,res,next)=>{
        let userrollno=req.params.rollno;
        userrollno=userrollno.toUpperCase();
        await ccolobj.deleteOne({rollno:userrollno});
        res.json("success");
}))

//invalid path
app.use((req,res,next)=>{
    res.json({message:req.url+" is invalid"});
})
//error handler
app.use((err,req,res,next)=>{
    res.json({message:err.message,description:"something went wrong"});
})

app.listen(4000,()=>{console.log("express api is running on port:4000")});