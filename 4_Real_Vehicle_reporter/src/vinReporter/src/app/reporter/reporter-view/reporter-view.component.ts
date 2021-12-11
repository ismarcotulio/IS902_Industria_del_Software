import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-reporter-view',
  templateUrl: './reporter-view.component.html',
  styleUrls: ['./reporter-view.component.css']
})
export class ReporterViewComponent implements OnInit {

  userVIN = "";

  constructor(
    private route: ActivatedRoute,
  ) { }

  ngOnInit(): void {
    this.getVehicleInfoByVIN()
  }

  getVehicleInfoByVIN(){
    this.route.params.subscribe(param => {
      this.userVIN = param["vin"]
    })
  }

}
