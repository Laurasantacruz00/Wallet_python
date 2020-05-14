from flask import Flask,render_template, request, redirect, url_for,jsonify
import hashlib,datetime,os,json, requests
from Transaccion import transaccion

#Creación de la aplicación 
app = Flask(__name__)

def hash_read(datos):
    return hashlib.sha256(datos.encode('utf-8')).hexdigest() #Funcion que genera el hash

@app.route("/wallet", methods=["GET", "POST"])#Ruta donde se hara la verificación de que la persona esta registrada
def ingreso():#Funcion la cual verifica si el archivo txt se encuentra lleno   
    if os.stat("wallet.txt").st_size == 0:
        print ("Vacio")
        return redirect(url_for('registro'))#Si este esta vacio se redirije a la pagina de registro
    else:
        print("lleno")#Si este esta lleno se redirije a la pagina de inicio
        return redirect(url_for('transaccion'))

@app.route("/Registro_wallet", methods=["GET", "POST"])#Registro de usuario
def registro():
    if request.method == 'POST':
        #Guardando datos del formulario
        palabras = request.form['name']#Nombre de usuario 
        correo = request.form['email']#Correo del usuario 
        hora_actual = datetime.datetime.now().time()#Hora de registro
        seed = str(palabras)+correo+str(hora_actual)#Informacion para generar el hash
        hash_origen = hash_read(seed)#Generando el hash
        seed = str(palabras)+correo+str(hora_actual)
        archivo = open("wallet.txt","w")#Creando txt con la información del cliente
        archivo.write("{}".format(seed) )
        archivo.close() 
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
        return redirect(url_for('transaccion'))
    return render_template("formulario.html")

        
@app.route("/saldo",methods=["GET","POST"])
def saldo():#Mostrando saldo al cliente
    r = requests.post('http://142.44.246.23:5596/coordinator',datos={"origen":"wallet","operacion":"consultarfondos"})#Pidiendo informacion al coordinador
    datos = r.get_json() #Respuesta del coordinador
    saldo = datos["saldo"]
    usuario = {'saldo':saldo}
    return render_template('Saldo.html', usuario = usuario)#Mostrando datos

@app.route("/validacion",methods=["GET","POST"])
def validacion_transaccion():#Validando informacion con el coordinador
    r = requests.post('http://142.44.246.23:5596/coordinator',datos=jsonify({"wallet":transaccion}))#Pidiendo validacion al coordinador
    datos = r.get_json() #Respuesta del coordinador
    respuesta = datos["respuesta"]
    if respuesta.upper()=="TRUE": #Si es true los datos son correctos la transaccion es exitosa
        usuario = {'transaccion':"Existoso"}
        return render_template('inicio.html', usuario = usuario)
        return redirect(url_for('saldo'))#Redireccionando a otra ruta
    else:
        usuario = {'transaccion':"Denegado"}#Si es false los datos son incorrectos la transaccion ha sido denegada
        return render_template('inicio.html', usuario = usuario)
        return redirect(url_for('transaccion'))#Redireccionando a otra ruta

@app.route("/transaccion", methods=["GET","POST"])#Realizando transaccion
def transaccion():
    with open('wallet.json') as contenido: #Leyendo el json creado anteriormente para ver la informacion del cliente
        datos_wallet = json.load(contenido)
        for dato in datos_wallet['datos']:
            hash_origen = dato['hash_origen']
    if request.method == 'POST':
        #Trayendo datos del formulario
        dir1 = hash_origen 
        dir2 = request.form['dir2']
        dinero = request.form['dinero']
        #Creando diccionario con la informacion de la transaccion
        transaccion = {
            "origen":"wallet",
            "operacion":"registrartransaccion",
            "dir1":str(dir1),
            "dir2":str(dir2),
            "dinero":str(dinero)
        }
        archivo = open("Transaccion.py","w")#Creando archivo aparte 
        archivo.write("transaccion = {}" .format(transaccion) )
        archivo.close() 
        return redirect(url_for('validacion_transaccion'))#Redireccionando a otra ruta
    usuario = {'name':hash_origen}#Trayendo hash del cliente
    return render_template('inicio.html', usuario = usuario)

if __name__ == '__main__':
    app.run(debug=True,port=4000)#Puerto y host donde se vera la api 