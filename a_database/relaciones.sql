--AREA RELACIONES
CREATE TABLE relaciones.roles(
	id serial primary key,
	nombre varchar(200)
);

CREATE TABLE relaciones.usuario(
	id serial primary key,
	rol_id int,
	nickname varchar(200),
	contrasena varchar(200),
	email varchar(200)
);


-- ALTER TABLE
ALTER TABLE relaciones.usuario ADD CONSTRAINT fk_usuario_rol FOREIGN KEY (rol_id) REFERENCES relaciones.roles (id) ON DELETE CASCADE ON UPDATE CASCADE;
