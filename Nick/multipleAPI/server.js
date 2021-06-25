const exp=require('express');
const app=exp();
const mc=require('mongodb').MongoClient;
const dburl="mongodb+srv://Nick:Nick@cluster0.xiwcb.mongodb.net/sampledb?retryWrites=true&w=majority";
mc.connect(dburl,{useNewUrlParser:true,useUnifiedTopology:true})
.then(client=>{
    const dbobj=client.db("sampledb")
    const uobj=dbobj.collection("userdata")
    const aobj=dbobj.collection("admindata")
    app.set("uobj",uobj);
    app.set("aobj",aobj);
    console.log("Database connected")
})
.catch(err=>{
    console.log('error in database connection',err)
})

const userobj=require('./APIs/userapi')
const adminobj=require('./APIs/adminapi')

app.use('/user',userobj)
app.use('/admin',adminobj)

//invalid path
app.use((err,req,res)=>{
    res.send({message:req.url+"is invalid path"})
})
//syntax error
 app.use((err,req,res,next)=>{
     res.send({message:err.message,description:"something went wrong"})
 })
app.listen(4000,()=>{console.log("server started on port 4000")})