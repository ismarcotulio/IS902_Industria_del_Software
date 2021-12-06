# -*- coding: utf-8 -*-
"""
    @author  mruizq@unah.hn
    @version 0.1.0
    @date 2021/10/29
"""

import json
import re
from bs4 import BeautifulSoup

class DataExtractor:

    def __init__(self):
        pass

    def getTablesFromHTML(self, html):
        pattern = re.compile(r'<table.*>[\s\S]*?<\/table>')
        matches = pattern.findall(html.text)

        return matches

    def getJsonFromTable(self, table):
        jsonList = []
        table_data = [[cell.text for cell in row("td")]
                         for row in BeautifulSoup(table, features="html.parser")("tr")]

        for i in table_data:
            tempJson = {}
            if len(i) > 2:
                date = i[0]
                tempJson.setdefault("sell_date", date)

                sellerInfo = re.split(", ",i[1])
                tempJson.setdefault("seller", sellerInfo[0])
                tempJson.setdefault("sell_location", sellerInfo[1])

                i[2] = re.sub("Listed for SaleListing ","", i[2])
                
                price = re.findall(r"Price: \$[0-9]*,?[0-9]*",i[2])
                if len(price)>0:
                    price = re.sub(r"Price: \$","",price[0])
                    tempJson.setdefault("price", price)
                
                mileage = re.findall(r"Mileage: [0-9]*,?[0-9]*",i[2])
                if len(mileage)>0:
                    mileage = re.sub(r"Mileage: ","",mileage[0])
                    tempJson.setdefault("vehicle_mileage", mileage)

                color = re.findall(r"Color: [A-Za-z]*",i[2])
                if len(color)>0:
                    color = re.sub(r"Color: ","",color[0])
                    tempJson.setdefault("vehicle_color", color)
            jsonList.append(tempJson)
                    
            
        return jsonList