const exp=require('express');
const userobj=exp.Router();
const bcryptjs=require('bcryptjs')
const errorhandler=require('express-async-handler')
userobj.get('/getusers',errorhandler(async (req,res)=>{
    let uobj=req.app.get("uobj")
    let users=await uobj.find().toArray()
    res.send({message:users})
}))
//body parser
userobj.use(exp.json())
userobj.post('/createuser',errorhandler(async (req,res)=>{
    let user=req.body
    let test=await userobj.findOne({username:user.username})
    if(test!=null){
        res.send({message:"user already existed"})
    }
    else{
        let hashedpw=await bcryptjs.hash(user.password,5)
        user.password=hashedpw
        await userobj.insertOne(user)
        res.send({message:"user added"})
    }
}))

module.exports=userobj