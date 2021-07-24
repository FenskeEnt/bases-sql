import sqlite3
from constantes import *

def conectar_db():
    conexion = sqlite3.connect(DATABASE_NAME)
    cursor = conexion.cursor()
    return conexion, cursor


def agregar_pelicula(pelicula):

    conexion, cursor = conectar_db()

    peli = (
        pelicula.nombre,
        pelicula.duracion,
        pelicula.genero
    )

    sql = f"INSERT INTO peliculas (nombre, duracion, genero) VALUES {peli};"
    cursor.execute(sql)

    conexion.commit()
    conexion.close()

def obtener_peliculas():
    conexion, cursor = conectar_db()
    sql = "SELECT * FROM peliculas;"
    cursor.execute(sql)
    peliculas = cursor.fetchall()
    conexion.close()
    return peliculas
