import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

// import { ChatPageRoutingModule } from './chat-routing.module';

import { ChatPage } from './chat.page';

import {AutosizeModule} from 'ngx-autosize';
import { RouterModule } from '@angular/router';
import {HttpClientModule} from '@angular/common/http';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    HttpClientModule,
    RouterModule.forChild([
    {
      path:'',
      component:ChatPage
    }
  ]),
  AutosizeModule
  ],
  declarations: [ChatPage]
})
export class ChatPageModule {}
