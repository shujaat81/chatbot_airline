import { ComponentsModule } from 'src/app/components/components.module';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonicModule } from '@ionic/angular';
import { WelcomePage } from './welcome.page';
import { RouterModule, Routes } from '@angular/router';
import { HttpClient, HttpParams, HttpClientModule } from '@angular/common/http';



const routes: Routes=[
  {
    path:'',
    component:WelcomePage
  }
]

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ComponentsModule,
    HttpClientModule,
    RouterModule.forChild(routes)
  ],
  declarations: [WelcomePage]
})
export class WelcomePageModule {}
