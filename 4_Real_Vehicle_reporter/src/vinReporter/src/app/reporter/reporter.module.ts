import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ReporterRoutingModule } from './reporter-routing.module';
import { ReporterViewComponent } from './reporter-view/reporter-view.component';


@NgModule({
  declarations: [
    ReporterViewComponent
  ],
  imports: [
    CommonModule,
    ReporterRoutingModule
  ]
})
export class ReporterModule { }
