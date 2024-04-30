--AREA PERSONAL
CREATE TABLE personal.jefe_area (
	id serial primary key,
	usuario_id int unique,
	nombre varchar(200),
	apellidos varchar(200),
	dni varchar(20)
);

CREATE TABLE personal.empleado(
	id serial primary key,
	usuario_id int unique,
	nombre varchar(200),
	apellidos varchar(200),
	dni varchar(20)
);
