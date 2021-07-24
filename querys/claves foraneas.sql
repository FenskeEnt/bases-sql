/*CREATE TABLE usuarios (
	id INTEGER NOT NULL,
	nombre TEXT NOT NULL,
	role INTEGER NOT NULL,
	PRIMARY KEY (id AUTOINCREMENT),
	FOREIGN KEY (role) REFERENCES roles (id)
);*/

/*CREATE TABLE roles (
	id INTEGER NOT NULL,
	nombre TEXT NOT NULL,
	PRIMARY KEY (id AUTOINCREMENT)
);*/

/*INSERT INTO roles (nombre) VALUES 
("cliente"),
("admin"),
("moderador");*/

INSERT INTO usuarios (nombre, role) VALUES 
("Gaston", 2),
("Sofia", 1),
("Martina", 1),
("Jose", 3),
("Lucas", 1),
("Gonzalo", 1);