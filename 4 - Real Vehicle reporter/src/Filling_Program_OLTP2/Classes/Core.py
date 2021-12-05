# -*- coding: utf-8 -*-
"""
    @author  mruizq@unah.hn
    @version 0.1.0
    @date 2021/10/28
"""

from Classes.MongoDB import MongoDB
from Classes.DataHandler import DataHandler
from Classes.CarMDHandler import CarMDHandler
from Classes.DataExtractor import DataExtractor
from datetime import datetime
from bson.json_util import dumps
import time
import re
import sys

class Core:

    def __init__(self):
        sys.stdout.write("\n---------------------PROGRAMA DE LLENADO NOSQL---------------------\n")
        sys.stdout.flush()
        sys.stdout.write("Gracias por utilizar el programa de llenado para la OLTP en Mongo! \n"+"Por favor espere, esto puede tardar algunos minutos..."+"\n\n")
        sys.stdout.flush()
        self.mongo = MongoDB()
        self.currentTime = datetime.utcnow()
        self.initTime = time.perf_counter()

    def run(self):
        if self.allowInsertion():
            self.insertVehiclesToMongo()
        else:
            print("Lo lamentamos, aun no pasan 24 Hrs desde su ultima insercion. Intentelo mas tarde o hasta el dia siguiente.")

    def allowInsertion(self):
        last = self.mongo.getLastItemFromCollection("meta_insertions")
        last = list(last)
        if len(last) > 0:
            last = datetime.strptime(last[0]['date'], '%Y-%m-%d %H:%M:%S.%f')
            passHours = int(((self.currentTime-last).total_seconds()/3600))
            if passHours < 24:
                return False
            else:
                return True
        else:
            return True
        
    
    def insertVehiclesToMongo(self):
        
        carMD = CarMDHandler()
        dataExtractor = DataExtractor()
        dataHandler = DataHandler(self.mongo, carMD, dataExtractor)
    
        limit = 50
        count = 0
        lastVerifiedPost = dataHandler.getLastVerifiedPost()
        postDataList = None
        sys.stdout.write("\n---------------------BUSCANDO VEHICULOS---------------------\n")
        sys.stdout.flush()
        sys.stdout.write("A continuacion se realizara una busqueda de "+str(limit)+" vehiculos que cummplan las siguientes condiciones: \n")
        sys.stdout.flush()
        sys.stdout.write("1-Su vin no debe existir en la coleccion de mongo\n")
        sys.stdout.flush()
        sys.stdout.write("2-Se debe verificar que el vin pertenezca a un vehiculo real\n")
        sys.stdout.flush()
        sys.stdout.write("2-Se debe verificar que existan reportes de la pagina https://vincheck.info/check/report-summary.php vinculados al vin\n\n")
        sys.stdout.flush()

    
        while count < limit:
            sys.stdout.write("Estado actual: "+str(count)+" vehiculos encontrados \n\n")
            sys.stdout.flush()
            if postDataList != None:
                lastPostNumber = postDataList[3]
            else:
                lastPostNumber = lastVerifiedPost
            postDataList = dataHandler.getLastValidPost(lastPostNumber)
            tables = postDataList[2]

            vehicleData = dataHandler.buildVehicleData(
                postDataList[0],
                postDataList[1],
                dataExtractor.getJsonFromTable(tables[3]),
            )
            self.mongo.insertToCollection(vehicleData, "vehicles")
            output_str = "Datos de vehiculo insertados en la BD! \n"+ str(vehicleData) + "\n\n"
            sys.stdout.write(output_str)
            sys.stdout.flush()
            count = count + 1
            dataHandler.updateLastVerifiedPost(postDataList[3])

        
        timeData = {}
        lastTime = time.perf_counter()
        timeData.setdefault("date", "{}".format(self.currentTime))
        timeData.setdefault("count", count)
        timeData.setdefault("time", "{}".format(lastTime - self.initTime))
        self.mongo.insertToCollection(timeData, "meta_insertions")
        print("\nSe han insertado {} vehiculos en la base de datos de MongoDB exitosamente.".format(count))

    
    
    