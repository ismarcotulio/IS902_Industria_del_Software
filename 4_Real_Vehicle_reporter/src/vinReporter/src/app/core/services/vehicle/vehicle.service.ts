import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Vehicle } from './../../models/vehicle/vehicle-model';

@Injectable({
  providedIn: 'root'
})
export class VehicleService {

  url1 = "http://3.141.15.155:4499/vehicle/only/"
  url2 = "AIzaSyDqRRUiuHrrHhrqd7y2TX94Rr5LrXyFKY8"

  constructor(private http: HttpClient) { }
  
  getVehicleByVIN(vin:string){
    return this.http.get<Vehicle[]>(`${this.url1}${vin}`)
  }
}
