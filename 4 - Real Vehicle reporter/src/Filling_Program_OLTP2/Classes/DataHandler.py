# -*- coding: utf-8 -*-
"""
    @author  mruizq@unah.hn
    @version 0.1.0
    @date 2021/10/28
"""

import json
import requests
import urllib
from datetime import datetime
import sys

class DataHandler:

    def __init__(self, mongo, carMD, dataExtractor):
        self.mongo = mongo
        self.carMD = carMD
        self.dataExtrator = dataExtractor

    
    def loadVINs(self):
        f = open("Collections/craigslists_car_posts.json")
        return json.load(f)

    def loadAccounts(self):
        f = open("Collections/carmd_accounts.json")
        return json.load(f)

    def getLastVerifiedPost(self):
        f = open("Collections/lastVerified.json")
        j = json.load(f)
        return int(j["last_post_verified"])

    def updateLastVerifiedPost(self, last):
        dict = {}
        dict.setdefault("last_post_verified", "{}".format(last))
        f = open("Collections/lastVerified.json", 'w')
        f.write(json.dumps(dict))
        
    def getVehicleInfo(self, vin):
        api = "https://vpic.nhtsa.dot.gov/api/vehicles/decodevinvalues/{}?format=json".format(vin)
        print(vin)
        print("")
        response = requests.get(api)
        return response.json()['Results'][0]

    def getVehicleInfoFromPage(self, vin):
        url = "https://vincheck.info/check/report-summary.php?vin={}".format(vin)
        payload={}
        headers = {
        'Cookie': 'PHPSESSID=c444umtqgbg3qkae1ot99m4dek; exp=v2; vin={}'.format(vin)
        }
        response = requests.request("GET", url, headers=headers, data=payload)  
        return response
    
    def VerifyVIN(self, vin):
        vehicleInfo = self.getVehicleInfo(vin)
        if vehicleInfo['ErrorCode'] == '0':
            vehicleInfoFromPage = self.getVehicleInfoFromPage(vin)
            tables = self.dataExtrator.getTablesFromHTML(vehicleInfoFromPage)
            if len(tables) > 0:
                return (True, vehicleInfo, tables)
            else:
                sys.stdout.write("Vehiculo con vin "+str(vin)+" no valido! no se encontraron reportes en https://vincheck.info/check/report-summary.php.\n")
                sys.stdout.flush()
                return False
        else:
            sys.stdout.write("Vehiculo con vin "+str(vin)+" no valido! No es un vehiculo real registrado en https://vpic.nhtsa.dot.gov/api/vehicles.\n")
            sys.stdout.flush()
            return False

    def getLastValidPost(self, lastPostNumber):
        state = 1
        count = lastPostNumber
        posts = self.loadVINs()['posts']
        post = None

        while state == 1:
            dataList =  self.VerifyVIN(posts[count]['vin'])  
            if dataList != False:
                if self.mongo.verifyCarInDB(posts[count]['vin']) == False:
                    post = posts[count]
                    state = 0
                    sys.stdout.write("Vehiculo con vin "+str(posts[count]['vin'])+" valido!\n\n")
                    sys.stdout.flush()
                else:
                    sys.stdout.write("Vehiculo con vin "+str(posts[count]['vin'])+" no valido! ya existe en la BD\n")
                    sys.stdout.flush()
            count = count + 1
        return (post, dataList[1], dataList[2], count) 
                    

    def getLastValidAccount(self):
        state = 1
        count = 0
        accounts = self.loadAccounts()['accounts']
        account = None
        while state == 1:
            creditsAccount = int(self.carMD.getAccount(
                accounts[count]['Authorization'],
                accounts[count]['partner-token'],
            ).acct_credits()['data']['credits'])
            if creditsAccount >= 5: 
                account = self.carMD.account
                state = 0      
            count = count + 1
        return account 

    def buildVehicleData(self, post, vehicleInfo, account, sellsData):
        vehicleDict = {}
        vehicleDict.setdefault("due_date","{}".format(datetime.utcnow()))
        vehicleDict.setdefault("posting_date",post['posting_date'])
        vehicleDict.setdefault("vin",vehicleInfo["VIN"])
        vehicleDict.setdefault("manufacter",vehicleInfo["Manufacturer"])
        vehicleDict.setdefault("brand",vehicleInfo["Make"])
        vehicleDict.setdefault("model",vehicleInfo["Model"])
        vehicleDict.setdefault("series",vehicleInfo["Series"])
        vehicleDict.setdefault("year",vehicleInfo["ModelYear"])
        vehicleDict.setdefault("fuel_type",vehicleInfo["FuelTypePrimary"])
        vehicleDict.setdefault("vehicle_type",vehicleInfo["VehicleType"])
        vehicleDict.setdefault("body_class",vehicleInfo["BodyClass"])
        vehicleDict.setdefault("base_price",vehicleInfo["BasePrice"])
        vehicleDict.setdefault("engine",vehicleInfo["EngineModel"])
        vehicleDict.setdefault("brake_system",vehicleInfo["BrakeSystemType"])
        vehicleDict.setdefault("number_cylinders",vehicleInfo["EngineCylinders"])
        vehicleDict.setdefault("displacement_cc",vehicleInfo["DisplacementCC"])
        vehicleDict.setdefault("doors",vehicleInfo["Doors"])
        vehicleDict.setdefault("sells_history",sellsData)
        my_vehicle = account.vin(post['vin'])
        vehicleDict.setdefault("maintenances",my_vehicle.maintenance(50000)['data'])      
        return vehicleDict

    def buildVehicleData(self, post, vehicleInfo, sellsData):
        vehicleDict = {}
        vehicleDict.setdefault("due_date","{}".format(datetime.utcnow()))
        vehicleDict.setdefault("posting_date",post['posting_date'])
        vehicleDict.setdefault("vin",vehicleInfo["VIN"])
        vehicleDict.setdefault("manufacter",vehicleInfo["Manufacturer"])
        vehicleDict.setdefault("brand",vehicleInfo["Make"])
        vehicleDict.setdefault("model",vehicleInfo["Model"])
        vehicleDict.setdefault("series",vehicleInfo["Series"])
        vehicleDict.setdefault("year",vehicleInfo["ModelYear"])
        vehicleDict.setdefault("fuel_type",vehicleInfo["FuelTypePrimary"])
        vehicleDict.setdefault("vehicle_type",vehicleInfo["VehicleType"])
        vehicleDict.setdefault("body_class",vehicleInfo["BodyClass"])
        vehicleDict.setdefault("base_price",vehicleInfo["BasePrice"])
        vehicleDict.setdefault("engine",vehicleInfo["EngineModel"])
        vehicleDict.setdefault("brake_system",vehicleInfo["BrakeSystemType"])
        vehicleDict.setdefault("number_cylinders",vehicleInfo["EngineCylinders"])
        vehicleDict.setdefault("displacement_cc",vehicleInfo["DisplacementCC"])
        vehicleDict.setdefault("doors",vehicleInfo["Doors"])
        vehicleDict.setdefault("sells_history",sellsData)     
        return vehicleDict
        

    