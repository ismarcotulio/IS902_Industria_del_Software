@author mruizq@unah.hn <br>
@version 1.0.0 <br>
@date 17/10/2021 <br>

# Modulo administrador de Aerolinea
<p>
Este modulo forma parte del framework odoo en su versionn 15.0. 

Dentro de este modulo se encuentran herramientas y componentes que permiten la administracion basica de una aerolinea.
</p>
<br>

### Algunas de las operaciones que incluye este modulo son:
* Registro de personas.
* Control de entrada y salida de personas.
<br><br>

### Los modelos del modulo se implementaron con base al siguiente diagrama de clases.
<br>
<img src="airlineDatabse.png"/>
<br><br>

instrucciones de ejecucion
---
<ol>
    <li>Clonar el repositorio <b>IS902_Industria_del_Software</b> a la par de la carpeta odoo</li>
    <li>Dentro de la carpeta odoo ejecutar el siguiente comando: 
    </li>

        ./odoo-bin --addons-path="addons/,../IS902_Industria_del_Software/2-tarea1/custom" -d [database_name] -i base -u airline_management
</ol>