from config import PostgresSQLPool
from flask import request
import traceback


class LogisticaModel:
    def __init__(self):
        self.db_pool = PostgresSQLPool()

    # TABLA MATERIAL
    def getRoles(self):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()

            query = cursor.execute(
                """
                SELECT * FROM relaciones.roles;
                """
            )
            # LISTA PARA RECIBIR LA DATA
            data = cursor.fetchall()

            datos = list()
            
            
            contenido = dict()

            for row in data:
                contenido = {
                    'id':row[0],
                    'nombre':row[1]
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

    def createRoles(self,nombre):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            INSERT INTO relaciones.roles (nombre) VALUES (%s);
            """,(nombre),True
            )
            return 'Rol created successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)
        

    def deleteRoles(self,nombre):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            DELETE FROM relaciones.roles WHERE nombre = %s;
            """,(nombre),True
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
