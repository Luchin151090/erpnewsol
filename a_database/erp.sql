CREATE SCHEMA logistica;


CREATE TABLE logistica.material(
	id serial primary key,
	codigo varchar(30),
	nombre varchar(300),
	descripcion varchar(1000),
	cantidad int,
	stock int,
	fecha_ingreso date
);