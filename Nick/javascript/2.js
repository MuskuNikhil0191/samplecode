var a=10
function fun(msg){
    console.log(msg)
}
module.exports.a=a
module.exports.fun=fun

let status=false
const promise=new Promise((resolve,reject)=>{
    if(status==true){
        setTimeout(()=>{
            resolve("hurry")
        },5000)
    }
    else{
        setTimeout(()=>{
            reject("sorry")
        },5000)
    }
})
promise.
then(value=>{
    console.log(value)
}).
catch(err=>{
    console.log(err)
})