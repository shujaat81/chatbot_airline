import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { FaresPageRoutingModule } from './fares-routing.module';

import { FaresPage } from './fares.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    FaresPageRoutingModule
  ],
  declarations: [FaresPage]
})
export class FaresPageModule {}
