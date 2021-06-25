class product{
    name:string;
    productno:number;
    brand:string;
    mrp:number;
    constructor(name:string,productno:number,brand:string,mrp:number){
        this.name=name;
        this.productno=productno;
        this.brand=brand;
        this.mrp=mrp;
    }
}
let obj1=new product("iphone 6s",1,"apple",30000);
let obj2=new product("samsung note",2,"samsung",25000);
let obj3=new product("redmi node 7pro",3,"redmi",10000);
let obj4=new product("vivo333",4,"vivo",15000);
let obj5=new product("honor 7lite",5,"honor",20000);
let objarr:any=[obj1,obj2,obj3,obj4,obj5];
for(let i of objarr){
    console.log(i)
}

class student{
    name:string;
    rollno:number;
    marks:number[];
    constructor(name:string,rollno:number,marks:number[]){
        this.name=name;
        this.rollno=rollno;
        this.marks=marks;
    }
}
let stud1=new student("nick",1,[91,92,93]);
let stud2=new student("sam",2,[81,82,83]);
let stud3=new student("chay",3,[74,75,76]);
let stud4=new student("jack",4,[88,87,90]);
let stud5=new student("rose",5,[70,90,80]);
let studarr:any=[stud1,stud2,stud3,stud4,stud5];
for(let i of studarr){
    console.log(i)
}
