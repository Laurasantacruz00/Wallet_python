# Wallet en python
	
La aplicacion se encuentra funcionando desde la URL:

	Mockup de Api: http://142.44.246.66:4000/wallet
	Api enlazada: http://142.44.246.66:5000/wallet
	
Para hacer pruebas con el mockup se recomienda el uso de Postman o insomnia en la cual se puede enviar una petición en formato json con el método post a los siguientes url de la siguiente forma:
	
	Enviar saldo: http://142.44.246.66:4000/saldo
		{
			"saldo":"el saldo que quiera agregar"
		}
	Registro de transaccion: http://142.44.246.66:4000/validacion
		{
			"respuesta":"true o false dependiendo de si fueron aceptados o denegados los datos"
		}
		
Esta api fue creada en python 3.6 usando los siguientes paquetes y librerías los cuales nos permitieron el funcionamiento correcto de la aplicación

	from flask import Flask,render_template, request, redirect, url_for,jsonify
	import hashlib,datetime,os,json

Estás, usadas con el objetivo de crear una aplicación web (Flask), generar un hash para el cliente (Hashlib), verificar la hora interna del equipo (datetime), librerías como "json" la cual nos permite generar un archivo del mismo tipo y requests que se encargará de hacer el envio y recepcion de datos a otras aplicaciones, así como "os" el cual nos permitirá verificar si el archivo txt (wallet.txt), está lleno o vacío para determinar si el cliente ya fue registrado previamente.

La aplicación fue creada con el objetivo realizar transacciones entre wallet's, para esto se genera un hash mediante el uso de 12 palabras, un correo registrado por el usuario y la hora de registro. Estos datos se guardaran en un diccionario.

	wallet_1 = {} #Creando un diccionario con la informacion del cliente 
        wallet_1['datos'] = []
        wallet_1['datos'].append({
            "palabras":str(palabras),
            "email":str(correo),
            "hora_actual":str(hora_actual),
            "hash_origen":str(hash_origen)
        })
        with open('wallet.json', 'w') as file:#Creando archivo json con la informacion del cliente
            json.dump(wallet_1, file, indent=4)

A Partir de esta información se hace la creación de un archivo json y un txt los cuales nos permitirán saber si el usuario se encuentra registrado en la plataforma, si el archivo txt está vacío entonces se procede a realizar el registro, si esta lleno el usuario ingresa a las transacciones.

Al registrarse el usuario se da paso al inicio de la aplicación en la cual se le da la opción al usuario de realizar una transacción, para esto se piden datos como hash de origen, hash de destino y el monto que desea enviar, y a partir de este se crea un diccionario que posteriormente se convertirá en un json el cual será enviado al coordinador

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

Para validar que los datos de la transacción sean correctos se hace el envío de la información ingresada por el cliente al coordinador por medio de un archivo json, el cual dependiendo de su respuesta "True" o "False" se le da un destino, si sus datos son erróneos el registro de transacción no será efectuado.

	r = requests.post('http://142.44.246.23:5596/coordinator',datos=jsonify({"wallet":transaccion}))
	datos = r.get_json() #Respuesta del coordinador
	respuesta = datos["respuesta"]
	
La wallet será ejecutada desde la dirección de host '142.44.246.66' por el puerto 5000, el envío y recepción de datos será realizado en las siguientes rutas:

Registro de transacción (Validación) y Información del usuario (Saldo):

	http://142.44.246.66:5000/transaccion	
