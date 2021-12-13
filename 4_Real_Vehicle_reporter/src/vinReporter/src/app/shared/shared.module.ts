import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {RouterModule} from "@angular/router";
import { HeaderDefaultComponent } from './components/header-default/header-default.component';

import { MaterialModule } from '../material/material.module';
import { CarouselComponent } from './components/carousel/carousel.component';



@NgModule({
  declarations: [
    HeaderDefaultComponent,
    CarouselComponent
  ],
  imports: [
    CommonModule,
    MaterialModule,
    RouterModule
  ],
  exports:[
    HeaderDefaultComponent,
    CarouselComponent
  ]
})
export class SharedModule { }
