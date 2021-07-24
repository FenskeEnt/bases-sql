CREATE TABLE clientes (
	id INTEGER NOT NULL,
	nombre TEXT NOT NULL,
	apellido TEXT NOT NULL,
	email TEXT NOT NULL,
	fecha_registro DATETIME NOT NULL,
	telefono INTEGER,
	PRIMARY KEY (id AUTOINCREMENT)
);
	
