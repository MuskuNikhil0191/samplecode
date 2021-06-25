import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { DataService } from '../data.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent{

  //ngform
  constructor(private ds:DataService){}
  userobj:any;
  getUserData(formobj:NgForm){
    this.userobj=formobj.value;
    this.ds.dataofservice.push(this.userobj);
    console.log(this.ds.dataofservice)
  }
  /** 
  delobj(inx:any){
    this.users.splice(inx,1)
  }
*/

}
