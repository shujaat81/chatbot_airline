import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { StartComponent } from './start/start.component';
import { LogoComponent } from './logo/logo.component';
import { IonicModule } from '@ionic/angular';
import { FormsModule } from '@angular/forms';
import { HomeRouter } from '../home/home.router';



@NgModule({
  declarations: [StartComponent,LogoComponent],
  exports:[StartComponent,LogoComponent],
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    
  ]
})
export class ComponentsModule { }
