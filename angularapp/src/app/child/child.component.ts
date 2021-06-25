import { Component, Input,OnInit, Output ,EventEmitter} from '@angular/core';

@Component({
  selector: 'app-child',
  templateUrl: './child.component.html',
  styleUrls: ['./child.component.css']
})
export class ChildComponent{
  @Input() recievingdata:any;
  emitingdata:string="nidhi";
  count:number=0
  @Output() myevent=new EventEmitter()
  senddata(){
    this.myevent.emit(this.emitingdata)
  }
  c1:boolean=true
  c2:boolean=true
  c3:boolean=true
  status:boolean=false
  msg:string="card is already selectd"
  selectcount(c:any){
    console.log(c)
    if(c=="c1"){
      if(this.c1){
        this.c1=!this.c1
        this.count+=1
        this.myevent.emit(this.count)
      }
      else{
        alert("Card is already selected!")
      }
    }
    else if(c=="c2"){
      if(this.c2){
        this.count+=1
        this.myevent.emit(this.count)
        this.c2=!this.c2
      }
      else{
        alert("Card is already selected!")
      }
    }
    else{
      if(this.c3){
        this.count+=1
        this.myevent.emit(this.count)
        this.c3=!this.c3
      }
      else{
        alert("Card is already selected!")
      }
    }
  }
}
