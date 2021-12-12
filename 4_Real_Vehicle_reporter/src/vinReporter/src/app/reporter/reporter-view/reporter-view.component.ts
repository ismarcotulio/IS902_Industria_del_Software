import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { Vehicle } from 'src/app/core/models/vehicle/vehicle-model';
import { VehicleService } from 'src/app/core/services/vehicle/vehicle.service';

@Component({
  selector: 'app-reporter-view',
  templateUrl: './reporter-view.component.html',
  styleUrls: ['./reporter-view.component.css']
})
export class ReporterViewComponent implements OnInit {
  vehicle?: Vehicle;
  userVIN = "";

  constructor(
    private route: ActivatedRoute,
    private vehicleService: VehicleService
  ) { }

  ngOnInit(): void {
    this.getVehicleInfoByVIN()
  }

  getVehicleInfoByVIN(){
    this.route.params.subscribe(param => {
      this.userVIN = param["vin"]

      this.vehicleService.getVehicleByVIN(this.userVIN).subscribe(
        data => {
          this.vehicle = data
          console.log(this.vehicle)
        }
      )
    })
  }

}
