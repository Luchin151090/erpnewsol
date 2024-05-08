-- ÁREA LOGISTICA
CREATE TABLE area.area_logistica(
	id serial primary key,
	nombre varchar(200),
	area_id int
);

CREATE TABLE logistica.subarea(
	id serial primary key,
	nombre varchar(300),
	responsable varchar(50),
	area_logistica_id int
);

CREATE TABLE logistica.fval(
	id serial primary key,
	nombre varchar(300),
	cantidad int,
	fecha_req date,
	solicitante varchar(50),
	area_solicitante varchar(50),
	area_logistica_id int
);

CREATE TABLE logistica.almacen(
	id serial primary key,
	nombre varchar(300),
	ubicacion varchar(50),
	area_logistica_id int
);


CREATE TABLE logistica.lotes(
	id serial primary key,
	cantidad int,
	fecha_vencimiento date,
	fecha_produccion date,
	hora_produccion time,
	almacen_id int,
	producto_id int
);


CREATE TABLE logistica.material(
	id serial primary key,
	codigo varchar(30),
	nombre varchar(300),
	descripcion varchar(1000),
	cantidad int,
	stock int,
	fecha_ingreso date,
	almacen_id int
);

CREATE TABLE logistica.equipo_herramienta(
	id serial primary key,
	stock int,
	fecha date,
	descripcion varchar(1000),
	cantidad int,
	codigo varchar(30),
	nombre varchar(300),
	almacen_id int
);

CREATE TABLE logistica.producto(
	id serial primary key,
	nombre varchar(200),
	descarga_id int
);

CREATE TABLE logistica.vehiculo(
	id serial primary key,
	nombre varchar(200),
	capacidad float,
	carga_neta float
);

CREATE TABLE logistica.descarga(
	id serial primary key,
	fecha_descarga date,
	mermas int,
	vehiculo_id int
);




-- ALTER TABLES AREA
ALTER TABLE area.area_logistica ADD CONSTRAINT fk_area_logistica_area FOREIGN KEY (area_id) REFERENCES area.area (id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE area.area ADD CONSTRAINT fk_area_jefe FOREIGN KEY (jefe_id) REFERENCES personal.jefe_area (id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE personal.empleado ADD CONSTRAINT fk_personal_area FOREIGN KEY(area_id) REFERENCES area.area(id) ON DELETE CASCADE ON UPDATE CASCADE;

-- ALTER TABLES LOGISTICA
ALTER TABLE logistica.subarea ADD CONSTRAINT fk_subarea_logistica FOREIGN KEY (area_logistica_id) REFERENCES area.area_logistica (id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE logistica.fval ADD CONSTRAINT fk_fval_logistica FOREIGN KEY (area_logistica_id) REFERENCES area.area_logistica (id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE logistica.almacen ADD CONSTRAINT fk_almacen_logistica FOREIGN KEY (area_logistica_id) REFERENCES area.area_logistica (id) ON DELETE CASCADE ON UPDATE CASCADE;

-- ALTER TABLE ALMACEN
ALTER TABLE logistica.material ADD CONSTRAINT fk_material_almacen FOREIGN KEY(almacen_id) REFERENCES logistica.almacen (id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE logistica.equipo_herramienta ADD CONSTRAINT fk_equipo_almacen FOREIGN KEY(almacen_id) REFERENCES logistica.almacen (id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE logistica.lotes ADD CONSTRAINT fk_lotes_almacen FOREIGN KEY(almacen_id) REFERENCES logistica.almacen (id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE logistica.lotes ADD CONSTRAINT fk_lotes_producto FOREIGN KEY(producto_id) REFERENCES logistica.producto (id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE logistica.descarga ADD CONSTRAINT fk_descarga_vehiculo FOREIGN KEY(vehiculo_id) REFERENCES logistica.vehiculo (id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE logistica.producto ADD CONSTRAINT fk_producto_descarga FOREIGN KEY() REFERENCES logistica.almacen (id) ON DELETE CASCADE ON UPDATE CASCADE;



