from modelos import Pelicula, Genero, Catalogo
import sql

def agregar_pelicula():
    nombre = str(input("Ingrese el nombre de la pelicula que desea agregar: "))
    duracion = int(input("Ingrese la duracion en minutos de la pelicula: "))
    genero = int(input("Ingrese el genero de la pelicula: "))
    pelicula = Pelicula(nombre, duracion, genero)
    sql.agregar_pelicula(pelicula)

catalogo = Catalogo("Peliculas de Mafia")
def obtener_peliculas():
    peliculas = sql.obtener_peliculas()
    for pelicula in peliculas:
        guardar_pelicula = Pelicula(pelicula[1], pelicula[2], pelicula[3])
        catalogo.peliculas.append(guardar_pelicula)

    for pelicula in catalogo.peliculas:
        print(f"""
Nombre de la pelicula: {pelicula.nombre}
Duracion de la pelicula: {pelicula.duracion} minutos
Genero de la pelicula: {pelicula.genero}""")