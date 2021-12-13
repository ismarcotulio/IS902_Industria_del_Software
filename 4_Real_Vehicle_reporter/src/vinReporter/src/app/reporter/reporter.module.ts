import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ReporterRoutingModule } from './reporter-routing.module';
import { ReporterViewComponent } from './reporter-view/reporter-view.component';
import { SharedModule } from '../shared/shared.module';
import { MaterialModule } from '../material/material.module';


@NgModule({
  declarations: [
    ReporterViewComponent
  ],
  imports: [
    CommonModule,
    ReporterRoutingModule,
    SharedModule,
    MaterialModule
  ]
})
export class ReporterModule { }
