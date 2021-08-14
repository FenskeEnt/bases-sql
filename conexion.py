import sqlite3

conexion = sqlite3.connect("basespruebacurso.db")
cursor = conexion.cursor()

def obtener_clientes():
    sql = "SELECT * FROM clientes;"
    cursor.execute(sql)
    clientes = cursor.fetchall()
    #print(clientes[0][1])
    for cliente in clientes:
        print(cliente)

def agregar_cliente(nombre, apellido, email, fecha_registro, roles, telefono=None):
    cliente = (
        nombre,
        apellido,
        email,
        fecha_registro,
        telefono,
        roles
    )
    sql = f"INSERT INTO clientes (nombre, apellido, email, fecha_registro, telefono, role) VALUES {cliente}"
    cursor.execute(sql)

def obtener_un_cliente(id):
    sql = f"SELECT * FROM clientes WHERE id = {id}"
    cursor.execute(sql)
    cliente = cursor.fetchone()
    print(cliente)

def editar_un_cliente(id, nombre):
    sql = f"UPDATE clientes SET nombre = '{nombre}' WHERE id = {id}"
    cursor.execute(sql)

def eliminar_cliente(id):
    sql = f"DELETE FROM clientes WHERE id = {id}"
    cursor.execute(sql)

#obtener_clientes()
agregar_cliente("Pia", "Mendoza", "correo@gmail.com", "2021-06-03 15:30:04.552583", "cliente")

conexion.commit()
conexion.close()