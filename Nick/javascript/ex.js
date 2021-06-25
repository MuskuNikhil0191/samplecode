const express=require('express');
const app=express();
const path=require('path');
const dburl="mongodb+srv://Nick:Nick@cluster0.xiwcb.mongodb.net/sampledb?retryWrites=true&w=majority"
const mc=require('mongodb').MongoClient;
const bcryptjs=require('bcryptjs')
const errorhandler=require('express-async-handler')
let cobj;
mc.connect(dburl,{useNewUrlParser:true,useUnifiedTopology:true},(err,client)=>{
    if(err){
        console.log("error in connection",err)
    }
    else{
        let dbobj=client.db("sampledb");
        cobj=dbobj.collection("sampledata");
        console.log("Database connection success")
    }
})
//using callback
app.get('/getusers',(req,res)=>{
    cobj.find().toArray((err,usersarr)=>{
        if(err){
            console.log("error in getting data",err)
        }
        else{
            res.send({message:usersarr})
        }
    })
})

app.get('/getuser/:username',(req,res)=>{
    cobj.findOne({username:req.params.username},(err,user)=>{
        if(err){
            console.log("error in getting user",err)
        }
        else{
            res.send()
        }
    })
})

//body parser middleware
app.use(exp.json())

app.post('/createuser',(req,res)=>{
    let user=req.body;
    bcryptjs.hash(user.password,5,(err,hashpw)=>{
        if(err){
            console.log('error in hasing password',err);
        }
        else{
            user.password=hashpw;
        }
        cobj.insertOne(user,(err,success)=>{
            if(err){
                console.log('error in inserting',err)
            }
            else{
                res.send({message:"insertion success"})
            }
        })
    })
})

app.put('/updateuser',(req,res)=>{
    let user=req.body;
    cobj.updateOne({username:user.username},{$set:{
        username:user.username,
        age:user.age,
        password:user.password
    }},(err,success)=>{
            if(err){
                console.log('error in update',err)
            }
            else{
                res.send({message:"update success"})
            }
        })
})

app.delete('/deleteuser/:username',(req,res)=>{
    cobj.deleteOne({username:req.params.username},(err,success)=>{
        if(err){
            console.log('error in deletion',err)
        }
        else{
            res.send({message:"deletion success"})
        }
    })
})
//using promise
app.get('/getuser',(req,res)=>{
    cobj.find().toArray()
    .then(users=>{
        res.send({message:users})
    })
    .catch(err=>{
        console.log('error in getting data',err)
    })
})

app.get('/getuser/:username',(req,res,next)=>{
    cobj.findOne({username:req.params.username})
    .then(user=>{
        res.send({message:user})
    })
    .catch(err=>{
        console.log('error in getting user',err) //next(err)
    })
})

app.createuser('/createuser',(req,res)=>{
    let user=req.body;
    bcryptjs.hash(user.password,5)
    .then(hashedpw=>{
        user.password=hashedpw;
        cobj.insertOne()
        .then(success=>res.send({message:'creation success'}))
        .catch(err=>{
            console.log('error in creation',err)
        })
    })
    .catch(err=>{
        console.log('error in hashing password',err)
    })
})

//using async and await

app.get('/getusers',errorhandler(async (req,res,next)=>{
    let users=await cobj.find().toArray()
    res.send({message:users})
}))

app.put('/updateuser',errorhandler(async (req,res,next)=>{
    let user=req.body
    let hashedpw=await bcryptjs.hash(user.password,5)
    user.password=hashedpassword
    await cobj.updateOne({username:user.username},{$set:{username:user.username,
        age:user.age,
        password:user.password}})
    res.send('update success')
}))
//invalid path
app.use((req,res,next)=>{
    res.send({message:`${req.url} is not available`})
})
 
//syntax error

app.use((err,req,res,next)=>{
    console.log({message:err.message,description:"something went wrong"})
})
/*
 mem=[{
     id:11,
     name:'nick'
 },
 {
     id:22,
     name:'ram'
 }]
middleware
const middlefun=(req,res,next)=>{
    console.log(`${req.protocol}://${req.get('host')}${req.originalUrl}`);
    next();
};
app.use(middlefun);

app.get('/home',(req,res)=>{
    res.json(mem)
})
//get single mem
app.get('/home/:id',(req,res)=>{
    const found=mem.some(mem=> mem.id==req.params.id)
    if(found){
        res.send(mem.filter(mem => mem.id==req.params.id));
    }
    else{
        res.send(`No member at the id ${req.params.id}`)
    }
})
//static folder
app.use(express.static(path.join(__dirname,'html')));

//  app.get('/',(req,res)=>{
//      res.send('hello world');
//      res.sendFile(path.join(__dirname,'html','1.html'))
//  })
*/

const PORT=process.env.PORT || 5000;
app.listen(PORT,()=>console.log(`server started on port: ${PORT}`))

