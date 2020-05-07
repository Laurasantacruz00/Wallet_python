# Wallet en python

Esta wallet fue creada en python 3.6 con el objetivo realizar transacciones entre wallet, para esto se genera un hash mediante el uso de 12 palabras, un correo registrado por el usuario, así como la hora de registro.

Para la consecución de la wallet utilizamos e importamos flask, hash, datetime, json, request, os etc.

from flask import Flask,render_template, request, redirect, url_for,jsonify
import hashlib,datetime,os,json


Con el objetivo de ejecutar los datos desde un server, realizar la conversión hash, verificar la hora interna del equipo, json la cual genera un archivo del mismo tipo y leerá los mismos request que se encargará de hacer la conexión con el server coordinator y os el cual verifica si el archivo txt, está lleno o vacío. 

A Partir de esta información se hace la creación de un archivo json y un txt
Los cuales nos permitirán saber si el usuario se encuentra registrado en la plataforma, si el archivo txt está vacío entonces se procede a realizar el registro, si esta lleno el usuario ingresa a las transacciones.


wallet = {
            "origen":"wallet",
            "palabras":str(palabras),
            "email":str(correo),
            "hora_actual":str(hora_actual),
            "hash_origen":hash_origen
        }



Para validar que los datos sean correctos se hace el envío de la información del cliente al coordinador el cual dependiendo de su respuesta "True" o "False" se le da un destino si sus datos son erróneos el registro no será efectuado.

una vez confirmados los datos se ingresa al sector de transacciones. se pide la wallet interna del usuario, la dirección wallet del usuario 2 y un monto de dinero.
esto se guarda en un archivo json donde se envía al coordinador la dirección uno más la Segunda dirección y el monto total


dir1 = request.form['dir1']
        dir2 = request.form['dir2']
        dinero = request.form['dinero']
        transaccion = {
            "dir1":str(dir1),
            "dir2":str(dir2),
            "dinero":str(dinero)
        }

La validación de estos datos será dada a partir de la respuesta del coordinador TRUE or FALSE esta misma será leída y será procesada para dar la respuesta al usuario por medio de un html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>Document</title>
</head>
<body>
    <div class="text-center">
        <h1 class="display-2">Wallet</h1>
        <hr>
    </div>    

{% block title %}{% endblock %}
{% block content %}
<div class="text-center">
    <h1 class="display-4">saldo </h1>
    <h2 class="display-4">Tu saldo es: {{usuario.saldo}}</h2>
    <br>
    <button onclick="window.location.href='/transaccion'" class="btn btn-primary">Volver</button>
</div>
{% endblock %}



<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>






La wallet será ejecutada desde la dirección de host '142.44.246.66' por el puerto 4000, el envío y recepción de datos será realizado en las siguientes rutas:
Validación de datos (registro y transacción):
	Registro:	http://142.44.246.66:4000/wallet_1
	Transacción:   http://142.44.246.66:4000/validacion
Información del usuario (Saldo):
	Saldo: 		http://142.44.246.66:4000/saldo
