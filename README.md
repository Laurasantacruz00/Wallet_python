# Wallet en python

Esta wallet fue creada en python 3.6 con el objetivo realizar transacciones entre wallet, para esto se genera un hash mediante el uso de 12 palabras, un correo registrado por el usuario, así como la hora de registro.

Para la consecución de la wallet utilizamos e importamos flask, hash, datetime, json, request, os etc.

	from flask import Flask,render_template, request, redirect, url_for,jsonify
	import hashlib,datetime,os,json


Con el objetivo de ejecutar los datos desde un server, realizar la conversión hash, verificar la hora interna del equipo, json la cual genera un archivo del mismo tipo y leerá los mismos request que se encargará de hacer la conexión con el server coordinator y os el cual verifica si el archivo txt, está lleno o vacío. 

A Partir de esta información se hace la creación de un archivo json y un txt
Los cuales nos permitirán saber si el usuario se encuentra registrado en la plataforma, si el archivo txt está vacío entonces se procede a realizar el registro, si esta lleno el usuario ingresa a las transacciones.

Para validar que los datos de la transaccion sean correctos se hace el envío de la información del cliente al coordinador el cual dependiendo de su respuesta "True" o "False" se le da un destino si sus datos son erróneos el registro no será efectuado.

una vez confirmados los datos se ingresa al sector de transacciones. se pide la wallet interna del usuario, la dirección wallet del usuario 2 y un monto de dinero.
esto se guarda en un archivo json donde se envía al coordinador la dirección uno más la Segunda dirección y el monto total


	dir1 = request.form['dir1']
        dir2 = request.form['dir2']
        dinero = request.form['dinero']
        transaccion = {
            "origen":"wallet",
            "operacion":"registrartransaccion",
            "dir1":dir1,
            "dir2":dir2,
            "dinero":dinero
        }

La validación de estos datos será dada a partir de la respuesta del coordinador TRUE or FALSE esta misma será leída y será procesada para dar la respuesta al usuario por medio de un html.

La wallet será ejecutada desde la dirección de host '142.44.246.66' por el puerto 4000, el envío y recepción de datos será realizado en las siguientes rutas:

Validación de datos (transacción) y Información del usuario (Saldo):

	Transacción:   	http://142.44.246.66:4000/validacion	
	Saldo:         	http://142.44.246.66:4000/saldo
