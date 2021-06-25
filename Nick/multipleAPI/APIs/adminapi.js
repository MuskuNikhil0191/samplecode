const exp=require('express');
const adminobj=exp.Router();
const errorhandler=require('express-async-handler')
adminobj.get('/getadmins',errorhandler(async (req,res,next)=>{
    let aobj=req.app.get("aobj")
    let admins=await aobj.find().toArray();
    res.send({message:admins})
}))




module.exports=adminobj