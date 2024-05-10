CREATE TABLE area.area_finanzas(
	id serial primary key,
	nombre varchar(200),
    area_id int
);

CREATE TABLE finanzas.control_asistencia(
    id serial primary key,
    hora_ingreso time,
    hora_salida time,
    fecha date,
    nombre_empleado varchar(200),
    cantidad_horas int,
    area_finanzas_id int
);

CREATE TABLE finanzas.fvac(
    id serial primary key,
    monto_ingreso float,
    monto_salida float,
    fecha date,
    area_finanzas_id int
);

CREATE TABLE finanzas.caja(
    id serial primary key,
    nombre_caja varchar(200),
    saldo_final float,
    saldo_inicial float,
    area_finanzas_id int
);

CREATE TABLE finanzas.transaccion(
    id serial primary key,
    fecha_transaccion date,
    monto float,
    caja_origen int,
    caja_destino int
);

-- ALTER TABLES AREA
ALTER TABLE area.area_finanzas ADD CONSTRAINT fk_area_finanzas_area FOREIGN KEY (area_id) REFERENCES area.area (id) ON DELETE CASCADE ON UPDATE CASCADE;

-- ALTER TABLES LOGISTICA
ALTER TABLE finanzas.control_asistencia ADD CONSTRAINT fk_control_asistencia_finanzas FOREIGN KEY (area_finanzas_id) REFERENCES area.area_finanzas (id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE finanzas.fvac ADD CONSTRAINT fk_fvac_finanzas FOREIGN KEY (area_finanzas_id) REFERENCES area.area_finanzas (id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE finanzas.caja ADD CONSTRAINT fk_caja_finanzas FOREIGN KEY (area_finanzas_id) REFERENCES area.area_finanzas (id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE finanzas.transaccion ADD CONSTRAINT fk_transaccion_origen FOREIGN KEY(caja_origen) REFERENCES finanzas.caja (id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE finanzas.transaccion ADD CONSTRAINT fk_transaccion_destino FOREIGN KEY(caja_destino) REFERENCES finanzas.caja (id) ON DELETE CASCADE ON UPDATE CASCADE;