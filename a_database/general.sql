-- SCHEMAS
CREATE SCHEMA logistica;
CREATE SCHEMA contabilidad;
CREATE SCHEMA area;
CREATE SCHEMA relaciones;
CREATE SCHEMA personal;
CREATE SCHEMA calidad;
CREATE SCHEMA administracion;
CREATE SCHEMA mantenimiento;
CREATE SCHEMA produccion;
CREATE SCHEMA comercial;
CREATE SCHEMA finanzas;


CREATE TABLE area.area(
	id serial primary key,
	codigo_area varchar(200),
    jefe_id int
);