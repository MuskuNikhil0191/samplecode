console.log("hello world")
let a:number=10
let b:boolean=true
let c:string="hello"
let o:object={name:"nikhil",age:20}
//array of numbers
let arr:number[]=[1,2,3]
//any type
let str:any="3l"
//tuple
let t:[string,number]=["hello",20]
console.log(a,b,c,o,arr,str,t)
interface person{
    firstname:string;
    lastname:string;
    age:number;
    readonly marks:number;//cannot be modified
}
let obj:person={firstname:"nikhil",lastname:"reddy",age:21,marks:333}
console.log(obj)
//function with normal,optional,default parameters
function fun(n:number,name?:string,lastname="reddy"):number{
    console.log(n,name,lastname);
    return n;
}
let x:number=fun(obj.age)
console.log(x)