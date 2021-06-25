import { Component, OnInit,OnDestroy } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit,OnDestroy{

   //lifecycle methods
   constructor(){
    console.log("constructor called")
  }
  ngOnInit(){
    console.log("ngOnInit called")
  }
  ngOnDestroy(){
    console.log("ngOnDestroy called")
  }

}
