import sqlite3
conexion = sqlite3.connect("basespruebacurso.db")
cursor = conexion.cursor()

def obtener_clientes():
    sql = "SELECT * FROM clientes;"
    cursor.execute(sql)
    clientes = cursor.fetchall()
    print(clientes[0][1])

def agregar_cliente(nombre, apellido, email, fecha_registro, role, telefono="Null"):
    sql = f"INSERT INTO clientes (nombre, apellido, email, fecha_registro, telefono, role) VALUES ('{nombre}', '{apellido}', '{email}', '{fecha_registro}', {telefono}, {role});"
    #print(sql)
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

#agregar_cliente("Mia", "Mendoza", "mia.com", "2021-06-03 15:30:04.552583", 1)
obtener_un_cliente(1)

conexion.commit()
conexion.close()