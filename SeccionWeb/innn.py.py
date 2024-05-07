#importamos todas las librerias necesarias
from flask import Flask, request, render_template, redirect, url_for,make_response

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash #las contraseñas se guardan en forma de hash,un toque de seguridad...

import webbrowser #esto es para que se abra automáticamente la página 
# Define la URL a abrir una vez que se abra el servidor
url = "http://localhost:5000/"

import mysql.connector
import tempfile
import time
import io
import os
import datetime

app = Flask(__name__) #instanciamos nuestro objeto Flask

'''
---------------------------------------------
------------CONFIGURACIONES------------------ 
---------------------------------------------
'''

# Configuración de la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="APPBD",
    consume_results=True
)

       

'''
---------------------------------------------
-------------SECCIÓN DE RUTAS---------------- 
---------------------------------------------
'''
#Acá van todas las rutas del proyecto, estas son funciones que responden al metodo "route" de nuestro objeto Flask, para 
#nuestro caso "app"
@app.route('/') #ruta principal
def home():
        return render_template('index.html', nombre="PEPE")
    
@app.route('/cursos') #ruta Solo de cursos
def  cursos():
    return render_template('cursos.html', nombre="identifiquese :)")
 
@app.route('/about') #acerca de...
def  about():
    return render_template('about.html', nombre="identifiquese :)")

@app.route('/contacto')
def  contacto():
    return render_template('contacto.html', nombre="identifiquese :)")
 
@app.route('/query') #esto es para unas pruebas, (en contrución)
def preguntas():
    return make_response('Hola mundo', 200)

@app.route('/InglesA1') 
def  InglesA1():
 #   if current_user.is_authenticated:
  #      try:       #este control de  errores es por si la sesión del usuario ha exppirado o intenta ingresar al curso sin pasar por login
    #        cursor = db.cursor()
     #       query = "SELECT InglesA1 FROM NotasExamenes WHERE id = %s"
      #      params = (idUsuario,)
       #     cursor.execute(query, params)
        #    NotaCurso = cursor.fetchone()[0]
         #   results = cursor.fetchall()
         #   cursor.close()  
          #  return render_template('BaseCursos.html',ExamenCurso="InglesA1Examen", NotaCurso=NotaCurso, nombre=NombreDelUsuario,NombreDelCurso="Inglés A1", ClasesDelCurso=["Bienvenida","Aula 1","Aula2","Aula3","Aula 4"],Aula0= {'Google': 'https://www.google.com', 'Bing': 'https://www.bing.com'},Aula1={},Aula2={},Aula3={},Aula4={},Aula5={},Aula6={},Aula7={},Aula8={},Aula9={},Aula10={})
       # except NameError:

    return redirect(url_for('home'))
@app.route('/InglesA1Examen', methods=['GET', 'POST'])
def InglesA1Examen():
     return redirect(url_for('PagEnConstrucion'))  
@app.route('/TortasFritas') 
def  TortasFritas():
         return redirect(url_for('home'))    

@app.errorhandler(404) #en caso de que el usuario se meta a un lugar que no existe
def page_not_found(error):
    # Redirige al usuario a la página de inicio después de 5 segundos
    Respuesta404 = make_response("Disculpe, no pudimos encontrar la página que busca ... Será redirigido al Inicio", 404)
    Respuesta404.headers['Refresh'] = '5;url=' + url_for('home')
    return Respuesta404
@app.route('/Upps', methods=['GET'])
def PagEnConstrucion():
    RespuestaConst = make_response("Disculpe, esto todavía está en contrucción... Será redirigido al Inicio", 404)
    RespuestaConst.headers['Refresh'] = '5;url=' + url_for('home')
    return RespuestaConst

'''
---------------------------------------------
------COMPROBACIONES Y PUESTA EN MARCHA------
---------------------------------------------
'''
print("Hola, esta aplicación web flask fue creada por Fabricio David Gallo")
if db.is_connected(): #Comprbación de conexión a mysql
    print("Conexión exitosa a la base de datos.")
else:
    print("No se pudo conectar a la base de datos.")

if __name__ == "__main__": #¿Nuestra objeto flask se instanció correctamente?
    webbrowser.open(url)
# Imprime un mensaje de éxito
    print(f"La URL {url} se ha abierto en correctamente")
    app.run(debug=True)    # entonces  ejecutar en modo debuggin
    

