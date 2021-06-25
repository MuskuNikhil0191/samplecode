var a=[1,2,3];
function arr(a){
    for(var i of a){
        var s=1;
        for(var j=2;j<Math.sqrt(i);j++){
            if(i%j==0){
                s=0;
                break;
            }
        }
        if(s==0)
            console.log(i+"Not Prime");
        else
            console.log(i+"Prime");
    }
}
arr(a);
student=[];
student.push({name:"nick",age:"18"});
student.push({name:"kick",age:"23"});
student.unshift({name:"new",age:"22"});
student.splice(2,1);
student.splice(1,1,{name:"fan",age:"11"});
student.splice(2,1,{name:"nick",age:"19"});
console.log(student);
var product={name:"bnw",price:100,discount:10};
console.log(product.discount/100*product.price);
let emp={name:"sam",basic:2500};
var hra=emp.basic*(15/100);
var da=emp.basic*(10/100);
console.log(da);
console.log(emp.basic+hra+da);