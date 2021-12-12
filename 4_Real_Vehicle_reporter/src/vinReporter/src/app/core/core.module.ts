import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { VehicleService } from './services/vehicle/vehicle.service';

@NgModule({
  declarations: [],
  imports: [
    CommonModule
  ],
  providers: [
    VehicleService
  ]
})
export class CoreModule { }
