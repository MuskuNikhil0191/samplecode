console.log("hello world");
var a = 10;
var b = true;
var c = "hello";
var o = { name: "nikhil", age: 20 };
//array of numbers
var arr = [1, 2, 3];
//any type
var str = "3l";
//tuple
var t = ["hello", 20];
console.log(a, b, c, o, arr, str, t);
var obj = { firstname: "nikhil", lastname: "reddy", age: 21, marks: 333 };
console.log(obj);
function fun(n, name, lastname) {
    if (lastname === void 0) { lastname = "reddy"; }
    console.log(n, name, lastname);
    return n;
}
var x = fun(obj.age);
console.log(x);
