import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AboutusComponent } from './aboutus/aboutus.component';
import { BootstrapComponent } from './bootstrap/bootstrap.component';
import { HomeComponent } from './home/home.component';
import { JavascriptComponent } from './javascript/javascript.component';
import { LoginComponent } from './login/login.component';
import { PagenotfoundComponent } from './pagenotfound/pagenotfound.component';
import { RegisterComponent } from './register/register.component';
import { TechnologiesComponent } from './technologies/technologies.component';
import { TypescriptComponent } from './typescript/typescript.component';

const routes: Routes = [
  {path:"home",component:HomeComponent},
  {path:"register",component:RegisterComponent},
  {path:"login",component:LoginComponent},
  {path:"aboutus",component:AboutusComponent},
  {path:"technologies",component:TechnologiesComponent,children:[
    {path:"bootstrap",component:BootstrapComponent},
    {path:"javascript",component:JavascriptComponent},
    {path:"typescript",component:TypescriptComponent}
  ]},
  {path:"",redirectTo:"/home",pathMatch:"full"},
  {path:"**",component:PagenotfoundComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
