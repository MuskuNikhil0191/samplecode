import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private hc:HttpClient){}
  dataofservice:any[]=[];
  getdata():Observable<any>{
    return this.hc.get("https://jsonplaceholder.typicode.com/todos");
  }
  getdata2():Observable<any>{
    return this.hc.get("https://jsonplaceholder.typicode.com/users");
  }
}
