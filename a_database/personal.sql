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
	dni varchar(20),
	area_id int
);

ALTER TABLE personal.jefe_area ADD CONSTRAINT fk_jefe_area_usuario FOREIGN KEY (usuario_id) REFERENCES relaciones.usuario (id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE personal.empleado ADD CONSTRAINT fk_empleado_usuario FOREIGN KEY (usuario_id) REFERENCES relaciones.usuario (id) ON DELETE CASCADE ON UPDATE CASCADE;