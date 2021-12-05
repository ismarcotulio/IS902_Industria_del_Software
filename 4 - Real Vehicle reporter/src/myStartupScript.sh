#!/bin/bash

    echo "---------------------------------------------------------------------------"
    echo "------------------------CREANDO BASE DE DATOS-------------------------------"
    echo "---------------------------------------------------------------------------"
    sleep 30s
    cd /opt/mssql-tools/bin && ./sqlcmd -S db -U SA -P "BD2_Grupo1" -Q "CREATE DATABASE CarDealership_OLTP1"
    echo "BASE DE DATOS CREADA"
    cd /var/www/html/Filling_Program_OLTP1/FAKERnodeJS
    echo "preparando el programa en node"
    npm install
    echo "---------------------------------------------------------------------------"
    echo "--------------EJECUTANDO PROGRAMA DE LLENADO EN NODEJS----------------------"
    echo "---------------------------------------------------------------------------"
    npm run dev
    echo "---------------------------------------------------------------------------"
    echo "--------------EJECUTANDO PROGRAMA DE LLENADO EN LARAVEL--------------------"
    echo "---------------------------------------------------------------------------"
    cd /var/www/html/Filling_Program_OLTP1
    php artisan migrate --seed
    echo "Gracias por la espera, base de datos llenada correctamente."
