import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'search'
})
export class SearchPipe implements PipeTransform {
  transform(data:any[],searchterm:string,searchbyterm:any):any{
    if(!data || !searchterm){
      return data;
    }
    else if(searchbyterm=="name"){
      return data.filter(obj=>obj.name.toLowerCase().indexOf(searchterm.toLowerCase())!==-1)
    }
    else if(searchbyterm=="username"){
      return data.filter(obj=>obj.username.toUpperCase().indexOf(searchterm.toUpperCase())!==-1)
    }
    else if(searchbyterm=="email"){
      return data.filter(obj=>obj.email.toUpperCase().indexOf(searchterm.toUpperCase())!==-1)
    }
    else if(searchbyterm=="id"){
        return data.filter(obj=>obj.id==Number(searchterm))
    }
  }
}
