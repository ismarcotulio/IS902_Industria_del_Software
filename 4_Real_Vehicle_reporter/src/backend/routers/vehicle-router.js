import express from 'express';
const Router = express.Router();
import { VehicleController } from '../controllers/vehicleController.mjs'

class VehicleRouter{
    
    constructor(database){
        this.database = database
        this.vehicleController = new VehicleController(database)
        Router.get('/only/:vin',this.getOnly)
    }
    
    

    getOnly = (req,res)=>{
        this.vehicleController.getVehicleInfo(req,res,req.params.vin)
    }
    
}

export {Router}
export {VehicleRouter}

