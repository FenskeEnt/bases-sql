import funciones

while True:

    menu = int(input("""
[1]Para agregar una nueva pelicula
[2]Para obtener peliculas
[0]Para salir del programa    
>>> """))

    if menu == 1:
        funciones.agregar_pelicula()
    elif menu == 2:
        funciones.obtener_peliculas()
    elif menu == 0:
        print("Saliendo del programa...")
        exit()