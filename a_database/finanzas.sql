CREATE TABLE area.area_finanzas(
	id serial primary key,
	nombre varchar(200),
	responsable_id int
);

CREATE TABLE finanzas.control_asistencia(
    id serial primary key,
    hora_ingreso time,
    hora_salida time,
    fecha date,
    nombre_empleado varchar(200),
    cantidad_horas int
);

CREATE TABLE finanzas.fvac(
    id serial primary key,
    monto_ingreso float,
    monto_salida float,
    fecha date
);

CREATE TABLE finanzas.caja(
    id serial primary key,
    nombre_caja varchar(200),
    saldo_final float,
    saldo_inicial float,
    caja_id int,
);

--ALTER TABLES
