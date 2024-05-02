-- ÁREA LOGISTICA
CREATE TABLE area.area_logistica(
	id serial primary key,
	nombre varchar(200),
	responsable_id int
);

CREATE TABLE area.area(
	id serial primary key,
	codigo_area varchar(200)
);

CREATE TABLE logistica.lotes(
	id serial primary key,
	cantidad int,
	fecha_vencimiento date,
	fecha_produccion date,
	hora_produccion time
);

CREATE TABLE logistica.jefe(
	id serial primary key,
	codigo_jefe varchar(200),
	nombre varchar(200),
	apellidos varchar(200),
	dni varchar(200)
);

CREATE TABLE logistica.empleado(
	id serial primary key,
	usuario_id int unique,
	nombre varchar(200),
	apellidos varchar(200),
	dni varchar(20)
);

CREATE TABLE logistica.material(
	id serial primary key,
	codigo varchar(30),
	nombre varchar(300),
	descripcion varchar(1000),
	cantidad int,
	stock int,
	fecha_ingreso date
);

CREATE TABLE logistica.equipo(
	id serial primary key,
	stock int,
	fecha date,
	descripcion varchar(1000),
	cantidad int,
	codigo varchar(30),
	nombre varchar(300)
);

CREATE TABLE logistica.almacen(
	id serial primary key,
	nombre varchar(300),
	ubicacion varchar(50)
);

CREATE TABLE logistica.subarea(
	id serial primary key,
	nombre varchar(300),
	responsable varchar(50)
);

CREATE TABLE logistica.fval(
	id serial primary key,
	nombre varchar(300),
	cantidad int,
	fecha_req date,
	solicitante varchar(50),
	area_solicitante varchar(50)
);
--subarea,fval,equipo,material