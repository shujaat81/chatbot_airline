import { Component, ViewChild, OnInit} from '@angular/core';
import { IonContent } from '@ionic/angular';
import {HttpClient} from '@angular/common/http';


@Component({
  selector: 'app-chat',
  templateUrl: './chat.page.html',
  styleUrls: ['./chat.page.scss'],
})
export class ChatPage implements OnInit{

  messages=[
    {
      user:'Ashis',
      createdAt: 1554090856000,
      msg:'Hey What are you doing'
    },
    {
      user:'Abi',
      createdAt: 1554090856000,
      msg:'Just coading something',
    },
    {
      user:'Ashis',
      createdAt: 1554090856000,
      msg:'Thats great',
    }
  ];

  currentUser ='Ashis';
  newMsg='';
  history=true;
  chat=false;
  hiscolor="#12d7e4";
  chatcolor="#ebebeb";

  @ViewChild(IonContent, {static: true}) content:IonContent 



  constructor(private httpObj:HttpClient) {

  }

  ngOnInit() {
    this.getdata();
  }
  getdata(){
  this.httpObj.get("http://localhost:3000/profile").subscribe(response=>{
   
    let replyobj=response as Object;
    this.messages.push(replyobj as any);

  })
}


sendMessage(){
    this.messages.push({
      user:'Ashis',
      createdAt:new Date().getTime(),
      msg:this.newMsg
    });
    this.newMsg='';

      setTimeout(()=>{
        this.newMethod();
      });
      
    
  }

  private newMethod() {
    this.content.scrollToBottom(200);
  }
}
