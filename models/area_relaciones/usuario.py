from config import PostgresSQLPool
from flask import request
import traceback


class LogisticaModel:
    def __init__(self):
        self.db_pool = PostgresSQLPool()

    # TABLA MATERIAL
    def getUsuario(self):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()

            query = cursor.execute(
                """
                SELECT * FROM relaciones.usuario;
                """
            )
            # LISTA PARA RECIBIR LA DATA
            data = cursor.fetchall()

            datos = list()
            
            
            contenido = dict()

            for row in data:
                contenido = {
                    'id':row[0],
                    'rol_id':row[1],
                    'nickname':row[2],
                    'contrasena':row[3],
                    'email':row[4]
                }
                datos.append(contenido)
                contenido={}
            return datos
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)

    def createUsuario(self,rol_id,nickname,contrasena,email):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            INSERT INTO relaciones.usuario (rol_id,nickname,contrasena,email) VALUES (%s,%s,%s,%s);
            """,(rol_id,nickname,contrasena,email),True
            )
            return 'Usuario created successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)
        

    def deleteUsuario(self,id):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            DELETE FROM relaciones.usuario WHERE id = %s;
            """,(id),True
            )
            return 'Rol deleted successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)
    
    def updateRoles(self,id,nombre):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            UPDATE relaciones.roles SET nombre=%s WHERE id=%s;
            """,(nombre,id),True
            )
            return 'Rol updated successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)

if __name__=="__main__":
    logistica_model = LogisticaModel()
