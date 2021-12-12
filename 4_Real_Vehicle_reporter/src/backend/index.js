import express from 'express';
import https from 'https';
import http from 'http';
import fs from 'fs';
import cors from 'cors';



import { Mongo } from './classes/mongo.mjs';


import { VehicleController } from './controllers/vehicleController.mjs';

import {Router,VehicleRouter} from './routers/vehicle-router.js';


//Configuracion express

//Instancia de express y llave maestra
var app = express()

var options = {
    key: fs.readFileSync('marco-key.pem'),
    cert: fs.readFileSync('marco-cert.pem')
};


//Instancia de base de datos
const database = new Mongo()



//Instancias de controladores
const vehicleController = new VehicleController(database);

//Instancia de routers
const vehicleRouter = new VehicleRouter(database)



//app.use(bodyParser.urlencoded({ extended: true }))
//app.use(bodyParser.json());
app.use(cors());
app.use('/vehicle', Router)


http.createServer(app).listen(3000, function(){
    console.log('HTTP listening on 3000');
});

https.createServer(options, app).listen(8080, function(){
    console.log('HTTPS listening on 8080');
});
