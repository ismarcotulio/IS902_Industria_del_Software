import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';


import { Mongo } from './classes/mongo.mjs';


import { VehicleController } from './controllers/vehicleController.mjs';

import {Router,VehicleRouter} from './routers/vehicle-router.js';


//Configuracion express

//Instancia de express y llave maestra
var app = express()


//Instancia de base de datos
const database = new Mongo()



//Instancias de controladores
const vehicleController = new VehicleController(database);

//Instancia de routers
const vehicleRouter = new VehicleRouter(database)



app.use(bodyParser.urlencoded({ extended: true }))
app.use(bodyParser.json());
app.use(cors());
app.use('/vehicle', Router)


app.listen(3000,()=>{
    console.log('Servidor iniciado en el puerto 3000') 
})
