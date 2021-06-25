var product = /** @class */ (function () {
    function product(name, productno, brand, mrp) {
        this.name = name;
        this.productno = productno;
        this.brand = brand;
        this.mrp = mrp;
    }
    return product;
}());
var obj1 = new product("iphone 6s", 1, "apple", 30000);
var obj2 = new product("samsung note", 2, "samsung", 25000);
var obj3 = new product("redmi node 7pro", 3, "redmi", 10000);
var obj4 = new product("vivo333", 4, "vivo", 15000);
var obj5 = new product("honor 7lite", 5, "honor", 20000);
var objarr = [obj1, obj2, obj3, obj4, obj5];
for (var _i = 0, objarr_1 = objarr; _i < objarr_1.length; _i++) {
    var i = objarr_1[_i];
    console.log(i);
}
var student = /** @class */ (function () {
    function student(name, rollno, marks) {
        this.name = name;
        this.rollno = rollno;
        this.marks = marks;
    }
    return student;
}());
var stud1 = new student("nick", 1, [91, 92, 93]);
var stud2 = new student("sam", 2, [81, 82, 83]);
var stud3 = new student("chay", 3, [74, 75, 76]);
var stud4 = new student("jack", 4, [88, 87, 90]);
var stud5 = new student("rose", 5, [70, 90, 80]);
var studarr = [stud1, stud2, stud3, stud4, stud5];
for (var _a = 0, studarr_1 = studarr; _a < studarr_1.length; _a++) {
    var i = studarr_1[_a];
    console.log(i);
}
