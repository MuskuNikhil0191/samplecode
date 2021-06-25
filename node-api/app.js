const exp=require('express');
const app=exp();
const bcryptjs=require('bcryptjs');
const errorhandler=require('express-async-handler');
const cors=require('cors');
const dburl="mongodb+srv://Nick:Nick@cluster0.6qtjq.mongodb.net/ajanthaseeds?retryWrites=true&w=majority"
//importing mongodb client
const mc=require('mongodb').MongoClient;
let colobj;
mc.connect(dburl,{useNewUrlParser:true,useUnifiedTopology:true})
.then(client=>{
    const dbobj=client.db("ajanthaseeds");
    colobj=dbobj.collection("users");
    console.log("DB connection success");

})
.catch(err=>{console.log("err in db connect",err)})
//bodyparser middleware
app.use(exp.json());
app.use(cors({origin:"http://localhost:4200"}));
app.get('/getusers',errorhandler(async (req,res,next)=>{
    // res.json({
    //     "statuscode":3000,
    //     "statusresponse":true
    // })
    let users=await colobj.find().toArray();
    res.json(users);

}))
app.get('/getuser/:email/:password',errorhandler(async (req,res,next)=>{
    let usermail=req.params.email;
    let userpwd=req.params.password;
    let exmail=await colobj.findOne({email:usermail});
    let expwd=await colobj.findOne({$and:[{email:usermail},{password:userpwd}]});
    if(exmail!=null && expwd!=null){
        res.json({message:"success",data:exmail});
    }
    else if(exmail==null){
        res.json({message:"Invalid email!"});
    }
    else{
        res.json({message:"Invalid password!"});
    }
}))

app.post('/createuser',errorhandler(async(req,res,next)=>{
    let user=req.body;
    let exuser=await colobj.findOne({email:user.email});
    if(exuser==null){
        // hashpw=await bcryptjs.hash(user.password,6);
        // user.password=hashpw;
        await colobj.insertOne(user);
        res.json({message:"success",data:user});
    }
    else{
        res.json({message:"Email already exists!"});
    }
}))
app.put('/updatepwd',errorhandler(async (req,res,next)=>{
    let usermail=req.body.email;
    let userpwd=req.body.password;
    exuser=await colobj.findOne({email:usermail});
    if(exuser!=null){
        await colobj.updateOne({email:usermail},{$set:{password:userpwd}});
        res.json("Successfully updated Password!");
    }
    else{
        res.json({message:"Invalid email!"});
    }
}))
app.delete('/deleteuser/:email',errorhandler(async (req,res,next)=>{
    let usermail=req.params.email;
    let exmail=await colobj.findOne({email:usermail});
    if(exmail!=null){
        await colobj.deleteOne({email:usermail});
        res.send({message:"User deleted!"});
    }
    else{
        res.send({message:"No user with given email exists!"});
    }
}))

//invalid path
app.use((req,res,next)=>{
    res.send({message:req.url+" is invalid"});
})

//error handler
app.use((err,req,res,next)=>{
    res.send({message:err.message,description:"something went wrong"})
})

app.listen(3000,()=>{
    console.log("Express Api is running at port 3000")
})