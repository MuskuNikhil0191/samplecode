import { Component, OnInit } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-aboutus',
  templateUrl: './aboutus.component.html',
  styleUrls: ['./aboutus.component.css']
})
export class AboutusComponent implements OnInit {

  constructor(private ds:DataService) { }
  resarr:any;
  n:number=10;
  searchterm:any;
  searchbyterm:any;
  ngOnInit(): void {
    this.ds.getdata2().subscribe(
      res=>{
        this.resarr=res;
      },
      err=>{
        console.log("err");
        alert("something went wrong");
      }
    )
  }
  searchby(s:any){
    this.searchbyterm=s;
  }
}
