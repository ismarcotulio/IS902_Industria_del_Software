import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderDefaultComponent } from './components/header-default/header-default.component';

import { MaterialModule } from '../material/material.module';



@NgModule({
  declarations: [
    HeaderDefaultComponent
  ],
  imports: [
    CommonModule,
    MaterialModule
  ],
  exports:[
    HeaderDefaultComponent
  ]
})
export class SharedModule { }
