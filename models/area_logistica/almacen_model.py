from config import PostgresSQLPool
from flask import request
import traceback

class AlmacenModel:
    def __init__(self):
        self.db_pool = PostgresSQLPool()
        
        # TABLA EQUIPO
    
    def getAlmacen(self):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()

            query = cursor.execute(
                """
                SELECT * FROM logistica.almacen;
                """
            )
            # LISTA PARA RECIBIR LA DATA
            data = cursor.fetchall()

            datos = list()
            
            
            contenido = dict()

            for row in data:
                contenido = {
                    'id':row[0],
                    'nombre':row[1],
                    'ubicacion':row[2]
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

    def createAlmacen(self,nombre,ubicacion):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            INSERT INTO logistica.almacen
              (nombre,ubicacion) VALUES (%s,%s);
            """,(nombre,ubicacion),True
            )
            return 'Almacen created successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)
        
    def deleteAlmacen(self,id):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            DELETE FROM logistica.almacen WHERE id = %s;
            """,(id),True
            )
            return 'Almacen deleted successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)
    
    def updateAlmacen(self,nombre,ubicacion,id):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            UPDATE logistica.almacen SET nombre=%s,ubicacion=%s WHERE id=%s;
            """,(nombre,ubicacion,id),True
            )
            return 'Almacen updated successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)

if __name__=="__main__":
    almacen_model = AlmacenModel()