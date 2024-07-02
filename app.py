#--------------------------------------------------------------------
#Instalar con pip install Flask
from flask import Flask, request, jsonify
#Instalar con pip install flask-cors
from flask_cors import CORS
#Instalar con pip install mysql-connector-python
import mysql.connector
# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename
#No es necesario instalar, es parte del sistema standard de Python
import os
import time
#--------------------------------------------------------------------

app = Flask(__name__)
CORS(app) # Esto habilitará CORS para todas las rutas

#--------------------------------------------------------------------
class Recetario: # Constructor de la clase
    def __init__(self, host, user, database):
        # Primero, establecemos una conexión sin especificar la base de datos
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=""
        )
        self.cursor = self.conn.cursor()
        # Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err
            
        # Una vez que la base de datos está establecida, creamos la tabla si no existe
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS receta (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            nombre VARCHAR(255) NOT NULL,
                            pais_origen VARCHAR(255) NOT NULL,
                            imagen VARCHAR(255) NOT NULL,
                            tipo VARCHAR(255),
                            tipo_alimentacion VARCHAR(255),
                            tiempo_coccion VARCHAR(255),
                            ingredientes TEXT NOT NULL,
                            preparacion TEXT NOT NULL,
                            destacada INT NOT NULL
                            )''')
        self.conn.commit()
        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)
    #----------------------------------------------------------------
    def recetas_agregar_datos(self, nombre, pais_origen, imagen, tipo, tipo_alimentacion, tiempo_coccion, ingredientes, preparacion, destacada):
        sql = "INSERT INTO receta (nombre, pais_origen, imagen, tipo, tipo_alimentacion, tiempo_coccion, ingredientes, preparacion, destacada) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = (nombre, pais_origen, imagen, tipo, tipo_alimentacion, tiempo_coccion, ingredientes, preparacion, destacada)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.lastrowid 
    #---------------------------------------------------------------- 
    def receta_detalle(self, id):
        self.cursor.execute(f"SELECT * FROM receta WHERE id = {id}")
        return self.cursor.fetchone()
    #----------------------------------------------------------------
    def recetas_modificar(self, id, nombre, pais_origen, imagen, tipo, tipo_alimentacion, tiempo_coccion, ingredientes, preparacion, destacada):
        sql = "UPDATE receta SET nombre = %s, pais_origen = %s, imagen = %s, tipo = %s, tipo_alimentacion = %s, tiempo_coccion = %s, ingredientes = %s, preparacion = %s, destacada = %s WHERE id = %s"
        valores = (nombre, pais_origen, imagen, tipo, tipo_alimentacion, tiempo_coccion, ingredientes, preparacion, destacada, id)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0
    #----------------------------------------------------------------
    def recetas_listar(self):
        self.cursor.execute("SELECT * FROM receta")
        recetas = self.cursor.fetchall()
        return recetas
    #----------------------------------------------------------------
    def recetas_listar_pais(self,id):
        if id == 1:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'Argentina'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 2:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'Bélice'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 3:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'Bolivia'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 4:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'Brasil'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 5:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'Chile'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 6:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'Colombia'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 7:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'Costa Rica'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 8:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'Cuba'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 9:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'Ecuador'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 10:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'El Salvador'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 11:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'Guatemala'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 12:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'Haití'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 13:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'Honduras'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 14:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'Mexico'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 15:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'Nicaragua'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 16:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'Panamá'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 17:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'Paraguay'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 18:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'Perú'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 19:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'Puerto Rico'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 20:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'República Dominicana'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 21:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'Uruguay'")
            recetas = self.cursor.fetchall()
            return recetas
        elif id == 22:
            self.cursor.execute(f"SELECT * FROM receta WHERE pais_origen = 'Venezuela'")
            recetas = self.cursor.fetchall()
            return recetas
    #----------------------------------------------------------------
    def recetas_eliminar(self,id):
        self.cursor.execute(f"DELETE FROM receta WHERE id = {id}")
        self.conn.commit()
        return self.cursor.rowcount > 0
    #----------------------------------------------------------------

#--------------------------------------------------------------------
# Cuerpo del programa
#--------------------------------------------------------------------
# Crear una instancia de la clase Catalogo
recetario = Recetario(host='localhost', user='root', database='recetas') 
#recetario = Recetario(host='willymiller41.mysql.pythonanywhere-services.com', user='willymiller41', password='WaM5d!J!uDZc!V7', database='willymiller41$recetas')
# Carpeta para guardar las imagenes.
ruta_destino = './static/img/public'
#ruta_destino = '/home/willymiller41/mysite/static/img/public/'
#Al subir al servidor, deberá utilizarse la siguiente ruta. USUARIO debe ser reemplazado por el
#nombre de usuario de Pythonanywhere #ruta_destino = '/home/USUARIO/mysite/static/imagenes'

#--------------------------------------------------------------------
# Index
#--------------------------------------------------------------------
@app.route("/", methods=["GET"])
def index():
    recetas = recetario.recetas_listar()
    return jsonify(recetas)
#--------------------------------------------------------------------
# Listar todos las recetas
#--------------------------------------------------------------------
@app.route("/recetas", methods=["GET"])
def recetas_listar():
    recetas = recetario.recetas_listar()
    return jsonify(recetas)
#--------------------------------------------------------------------
# Listar todos las recetas por país
#--------------------------------------------------------------------
@app.route("/recetas_pais/<int:id>", methods=["GET"])
def recetas_listar_pais(id):
    recetas = recetario.recetas_listar_pais(id)
    return jsonify(recetas)
#--------------------------------------------------------------------
# Mostrar una receta según su código
#--------------------------------------------------------------------
@app.route("/recetas/<int:id>", methods=["GET"])
def recetas_detalle(id): 
    receta = recetario.receta_detalle(id)
    if receta:
        return jsonify(receta), 201
    else:
        return "Receta no encontrada", 404
#--------------------------------------------------------------------
# Agregar una receta
#--------------------------------------------------------------------
@app.route("/recetas", methods=["POST"])
def recetas_agregar():
    #Recojo los datos del form
    nombre = request.form['nombre']
    pais_origen = request.form['pais_origen']
    imagen = request.files['imagen']
    tipo = request.form['tipo']
    tipo_alimentacion = request.form['tipo_alimentacion']
    tiempo_coccion = request.form['tiempo_coccion']
    destacada = request.form['destacada']
    ingredientes = request.form['ingredientes']
    preparacion = request.form['preparacion']
    nombre_imagen = ""
    # Genero el nombre de la imagen
    nombre_imagen = secure_filename(imagen.filename)
    # Chequea el nombre del archivo de la imagen, asegurándose de que sea seguro para guardar en el sistema de
    # archivos
    nombre_base, extension = os.path.splitext(nombre_imagen)
    # Separa el nombre del archivo de su extensión.
    nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"
    # Genera un nuevo nombre para la imagen usando un timestamp, para evitar sobreescrituras y conflictos de nombres.
    nuevo_id = recetario.recetas_agregar_datos(nombre, pais_origen, nombre_imagen, tipo, tipo_alimentacion, tiempo_coccion, ingredientes, preparacion, destacada)
    if nuevo_id:
        imagen.save(os.path.join(ruta_destino, nombre_imagen))
        # Si la receta se agrega con éxito, se devuelve una respuesta JSON con un mensaje de éxito y un
        # código de estado HTTP 201 (Creado).
        return jsonify({"mensaje": "Receta agregada correctamente.", "id": nuevo_id, "imagen": nombre_imagen}), 201
    else:
        # Si la receta no se puede agregar, se devuelve una respuesta JSON con un mensaje de error y un código
        # de estado HTTP 500 (Internal Server Error).
        return jsonify({"mensaje": "Error al agregar la receta."}), 500
#--------------------------------------------------------------------
# Modificar una receta según su código
#-------------------------------------------------------------------- 
#@app.route("/recetas/<int:id>", methods=["PUT"])
@app.route("/recetas_modificar/<int:id>", methods=["POST"])
def recetas_modificar(id):
    # Se recuperan los nuevos datos del formulario
    nuevo_nombre = request.form.get("nombre")
    nuevo_pais_origen = request.form.get("pais_origen")
    nuevo_tipo = request.form.get("tipo")
    nuevo_tipo_alimentacion = request.form.get("tipo_alimentacion")
    nuevo_tiempo_coccion = request.form.get("tiempo_coccion")
    nuevo_ingredientes = request.form.get("ingredientes")
    nuevo_preparacion = request.form.get("preparacion")
    nuevo_destacada = request.form.get("destacada")
    # Verifica si se proporcionó una nueva imagen
    if 'imagen' in request.files:
        imagen = request.files['imagen']
        # Procesamiento de la imagen
        nombre_imagen = secure_filename(imagen.filename)
        # Chequea el nombre del archivo de la imagen, asegurándose de que sea seguro para guardar en el sistema
        # de archivos
        nombre_base, extension = os.path.splitext(nombre_imagen)
        # Separa el nombre del archivo de su extensión.
        nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"
        # Genera un nuevo nombre para la imagen usando un timestamp, para evitar sobreescrituras y conflicto de nombres.
        # Guardar la imagen en el servidor
        imagen.save(os.path.join(ruta_destino, nombre_imagen))
        # Busco la receta guardada
        receta = recetario.receta_detalle(id) 
        if receta:
            # Si existe la receta... 
            imagen_vieja = receta["imagen"]
            # Armo la ruta a la imagen
            ruta_imagen = os.path.join(ruta_destino, imagen_vieja)
            # Y si existe la borro. 
            if os.path.exists(ruta_imagen):
                os.remove(ruta_imagen)
    else: 
        # Si no se proporciona una nueva imagen, simplemente usa la imagen existente del producto
        receta = recetario.receta_detalle(id)
        if receta:
            nombre_imagen = receta["imagen"]
        # Se llama al método recetas_modificar pasando el codigo de la receta y los nuevos datos.
    if recetario.recetas_modificar(id, nuevo_nombre, nuevo_pais_origen, nombre_imagen, nuevo_tipo, nuevo_tipo_alimentacion, nuevo_tiempo_coccion, nuevo_ingredientes, nuevo_preparacion, nuevo_destacada):
        # Si la actualización es exitosa, se devuelve una respuesta JSON con un mensaje de éxito y un
        # código de estado HTTP 200 (OK).
        return jsonify({"mensaje": "Receta modificada"}), 200
    else:
        # Si el receta no se encuentra (por ejemplo, si no hay ninguna receta con el código dado), se devuelve
        # un mensaje de error con un código de estado HTTP 404 (No Encontrado).
        return jsonify({"mensaje": "Receta no encontrada"}), 403
#--------------------------------------------------------------------
# Eliminar una receta según su código
#--------------------------------------------------------------------
#@app.route("/recetas/<int:codigo>", methods=["DELETE"])
@app.route("/recetas_eliminar/<int:id>")
# La ruta Flask /recetas/<int:codigo> con el método HTTP DELETE está diseñada para eliminar una receta
# específico de la base de datos, utilizando su código como identificador. #La función receta_eliminar se
# asocia con esta URL y es llamada cuando se realiza una solicitud DELETE a /recetas/ seguido de un número
# (el código de la receta).
def recetas_eliminar(id):
    # Busco la receta en la base de datos
    receta = recetario.receta_detalle(id)
    if receta:
        # Si la receta existe, verifica si hay una imagen asociada en el servidor.
        # Armo la ruta a la imagen
        ruta_imagen = os.path.join(ruta_destino, receta["imagen"])
        # Y si existe, la elimina del sistema de archivos.
        if os.path.exists(ruta_imagen):
            os.remove(ruta_imagen) 
            # Luego, elimina la receta del catálogo
            if recetario.recetas_eliminar(id):
                # Si la receta se elimina correctamente, se devuelve una respuesta JSON con un mensaje de éxito
                # y un código de estado HTTP 200 (OK).
                return jsonify({"mensaje": "Receta eliminado"}), 200
            else:
                # Si ocurre un error durante la eliminación (por ejemplo, si el producto no se puede eliminar
                # de la base de datos por alguna razón), se devuelve un mensaje de error con un código de
                # estado HTTP 500 (Error Interno del Servidor).
                return jsonify({"mensaje": "Error al eliminar la receta"}), 500 
        else:
            # Si la receta no se encuentra (por ejemplo, si no existe una receta con el codigo proporcionado),
            # se devuelve un mensaje de error con un código de estado HTTP 404 (No Encontrado).
            return jsonify({"mensaje": "Receta no encontrada"}), 404
#--------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)