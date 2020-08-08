import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {AlertController} from '@ionic/angular'
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable, Subscriber } from 'rxjs';

@Component({
  selector: 'app-welcome',
  templateUrl: './welcome.page.html',
  styleUrls: ['./welcome.page.scss'],
})
export class WelcomePage implements OnInit 
{
  public postData={
    username:'',
    password:''
  }
  alert: any;
 
  
  constructor(private router:Router,private alertController:AlertController,public http:HttpClient) { }
  
  ngOnInit() {
  
  }

checkin="";
public checkData(username: string, password: string)  {  
const body = { 'username': username, 'password': password }
var data = JSON.stringify(body);  
let header:HttpHeaders = new HttpHeaders().set('Content-Type', 'application/json');  
this.http.post('http://127.0.0.1:8080/login',data,{headers:header}).subscribe(async response => {
 console.log("repsonse",response);
 this.checkin=response as string;
 if(this.checkin==="true")
 {
   this.router.navigate(['/home/fares']);
 }
 else{
   
  const alert = await this.alertController.create({
    header:'Error',
    subHeader:'Incorrect UserName or Password',
    message:'Try with correct username and password',
    buttons:['OK']
    
  });
  await alert.present();
  
 }
})


  
}

  validateInput(){
    let username=this.postData.username.trim();
    let password=this.postData.password.trim();

    return(this.postData.username && this.postData.password && username.length>0 && password.length>0)
  }
  async navigateToFaresPage()
  {
    if (this.validateInput()){
      var checkthis=this.checkData(this.postData.username, this.postData.password)
      }
    else{
      const alert = await this.alertController.create({
        header:'Alert',
        subHeader:'Give UserName and Password',
        message:'These field are mandatory to SignIn',
        buttons:['OK']
        
      });
      await alert.present();
    }
  }


  clearInput()
  {
    var a=document.getElementById('username') as HTMLInputElement;
    var b=document.getElementById('password') as HTMLInputElement;
    a.value = '';
    b.value='';
  };
}


