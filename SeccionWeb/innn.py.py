#importamos todas las librerias necesarias
from flask import Flask, request, render_template, redirect, url_for,make_response,jsonify


import webbrowser #esto es para que se abra automáticamente la página 
# Define la URL a abrir una vez que se abra el servidor
url = "http://localhost:5000/"

import mysql.connector
app = Flask(__name__) #instanciamos nuestro objeto Flask

'''
---------------------------------------------
------------CONFIGURACIONES------------------ 
---------------------------------------------
'''

# Configuración de la base de datos
# Configuración de la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",  #Cambia Esto según tu usuario y contraseña
    password="root", # de Mysql
    database="AppMicro",
    consume_results=True
)
data = {'Movimiento': [], 'ReyBlanco': [], 'ReyNegro': [],'NumeroDeMovimiento':[],}
def EnviarAMysql(Dato1, Dato2, Dato3,Dato4, TablaDestino):
    try:
        cursor = db.cursor()
        query = f"INSERT INTO {TablaDestino} (Movimiento, ReyBlanco, ReyNegro,NumeroDeMovimiento) VALUES (%s, %s, %s, %s)"
        values = (Dato1, Dato2, Dato3,Dato4)
        cursor.execute(query, values)
        db.commit()
        print(f"Valores insertados correctamente en la tabla {TablaDestino}.")
    except Exception as e:
        print(f"Error al insertar valores: {str(e)}")
        db.rollback()  # Rollback en caso de excepción



    try:
        content = request.get_json()
        gasto = content['gasto']
        presion = content['presion']
        vibracion = content['vibracion']
        # Si no existe, agrega los nuevos valores
        data['gasto'].append(gasto)
        data['presion'].append(presion)
        data['vibracion'].append(vibracion)
        print(f"Added new data: gasto={gasto}, presion={presion}, vibracion={vibracion}")
        EnviarAMysql(gasto, presion, vibracion, TablaDestino)
        return jsonify({'success': True})
    except Exception as e:
        print(f"Error receiving data: {str(e)}")
        return jsonify({'success': False, 'error': str(e)})
       

'''
---------------------------------------------
-------------SECCIÓN DE RUTAS---------------- 
---------------------------------------------
'''
#Acá van todas las rutas del proyecto, estas son funciones que responden al metodo "route" de nuestro objeto Flask, para 
#nuestro caso "app"
@app.route('/') #ruta principal
def home():
        return render_template('index.html')
    
@app.route('/cursos') #ruta Solo de cursos
def  cursos():
    return render_template('cursos.html')
 
@app.route('/about') #acerca de...
def  about():
    return render_template('about.html')

@app.route('/contacto')
def  contacto():
    return render_template('contacto.html')
 
@app.route('/query') #esto es para unas pruebas, (en contrución)
def preguntas():
    return make_response('Hola mundo', 200)
 

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
print("Hola, esta aplicación web flask fue creada por Emanuel Suffo y Fabricio David Gallo")
if db.is_connected(): #Comprbación de conexión a mysql
    print("Conexión exitosa a la base de datos.")
else:
    print("No se pudo conectar a la base de datos.")


@app.route('/data1', methods=['POST'])
def receive_data1():
   TablaDestino="JugadaUno"
   if request.method == 'POST':
        # Obtener los datos enviados como JSON
        datos = request.get_json()
        # Acceder a los valores específicos
        Movimiento = datos.get("Movimiento")
        ReyBlanco = datos.get("ReyBlanco")
        ReyNegro = datos.get("ReyNegro")
        NumeroDeMovimiento= datos.get("NumeroDeMovimiento")
        EnviarAMysql(Movimiento, ReyBlanco, ReyNegro,NumeroDeMovimiento, TablaDestino)
        return jsonify({'success': True})
@app.route('/data2', methods=['POST'])
def receive_data2():
     TablaDestino="JugadaDos"
     if request.method == 'POST':
        # Obtener los datos enviados como JSON
        datos = request.get_json()
        # Acceder a los valores específicos
        Movimiento = datos.get("Movimiento")
        ReyBlanco = datos.get("ReyBlanco")
        ReyNegro = datos.get("ReyNegro")
        NumeroDeMovimiento= datos.get("NumeroDeMovimiento")
        EnviarAMysql(Movimiento, ReyBlanco, ReyNegro,NumeroDeMovimiento, TablaDestino)
        return jsonify({'success': True})
   
@app.route('/data3', methods=['POST'])
def receive_data3():
    TablaDestino="JugadaTres"
    if request.method == 'POST':
        # Obtener los datos enviados como JSON
        datos = request.get_json()
        # Acceder a los valores específicos
        Movimiento = datos.get("Movimiento")
        ReyBlanco = datos.get("ReyBlanco")
        ReyNegro = datos.get("ReyNegro")
        NumeroDeMovimiento= datos.get("NumeroDeMovimiento")
        EnviarAMysql(Movimiento, ReyBlanco, ReyNegro,NumeroDeMovimiento, TablaDestino)
        return jsonify({'success': True})
   
@app.route('/data4', methods=['POST'])
def receive_data4():
    TablaDestino="JugadaCuatro"
    if request.method == 'POST':
        # Obtener los datos enviados como JSON
        datos = request.get_json()
        # Acceder a los valores específicos
        Movimiento = datos.get("Movimiento")
        ReyBlanco = datos.get("ReyBlanco")
        ReyNegro = datos.get("ReyNegro")
        NumeroDeMovimiento= datos.get("NumeroDeMovimiento")
        EnviarAMysql(Movimiento, ReyBlanco, ReyNegro,NumeroDeMovimiento, TablaDestino)
        return jsonify({'success': True})
    
@app.route('/datadelete1') #esto es para unas pruebas, (en contrución)
def DeleteData1():
    cursor = db.cursor(dictionary=True)
    query = "DELETE  FROM JugadaUno"
    cursor.execute(query)
    result = cursor.fetchall() # Esto es obligtorio, consumir los datos, aunque sea vacío
    return make_response('Tabla Eliminada con Exito', 200)
@app.route('/get_data')
def get_data():
    try:
        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM EjemploUno"
        cursor.execute(query)
        result = cursor.fetchall()

        # Crear una tabla HTML
        table_html = "<table><tr><th>Gasto</th><th>Presión</th><th>Vibración</th></tr>"
        for row in result:
            table_html += f"<tr><td>{row['gasto']}</td><td>{row['presion']}</td><td>{row['vibracion']}</td></tr>"
        table_html += "</table>"

        return table_html
    except Exception as e:
        print(f"Error al obtener datos: {str(e)}")
        return jsonify({'error': str(e)})
@app.route('/data_page')
def data_page():
    try:
        cursor = db.cursor(dictionary=True)
        query = "SELECT * FROM JugadaUno"
        cursor.execute(query)
        result = cursor.fetchall()
        return render_template('data.html', data=result)
    except Exception as e:
        print(f"Error al obtener datos: {str(e)}")
        return jsonify({'error': str(e)})

if __name__ == "__main__": #¿Nuestra objeto flask se instanció correctamente?
    webbrowser.open(url)   # Abre la pagina
# Imprime un mensaje de éxito
    print(f"La URL {url} se ha abierto en correctamente")
    app.run(debug=False, host='0.0.0.0')    # entonces  ejecutar el servidor
    print(f"Servidor iniciado con exito UwU ")