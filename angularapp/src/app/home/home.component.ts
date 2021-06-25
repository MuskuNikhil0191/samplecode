import { Component, OnInit,OnDestroy } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent{

   //lifecycle methods
   dataofhome:string="hello";
   data:any;
   constructor(private ds:DataService){
  }
  senddata(data:any){
    this.ds.dataofservice=data;
  }
  getdata(){
    this.data=this.ds.dataofservice;
  }
}
