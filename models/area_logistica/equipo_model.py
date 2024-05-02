from config import PostgresSQLPool
from flask import request
import traceback

class EquipoModel:
    def __init__(self):
        self.db_pool = PostgresSQLPool()
        
        # TABLA EQUIPO
    
    def getEquipo(self):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()

            query = cursor.execute(
                """
                SELECT * FROM logistica.equipo;
                """
            )
            # LISTA PARA RECIBIR LA DATA
            data = cursor.fetchall()

            datos = list()
            
            
            contenido = dict()

            for row in data:
                contenido = {
                    'id':row[0],
                    'stock':row[1],
                    'fecha':row[2],
                    'descripcion':row[3],
                    'cantidad':row[4],
                    'codigo':row[5],
                    'nombre':row[6]
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

    def createEquipo(self,stock,fecha,descripcion,cantidad,codigo,nombre):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            INSERT INTO logistica.equipo (stock,fecha,descripcion,cantidad,codigo,nombre) VALUES (%s,%s,%s,%s,%s,%s);
            """,(codigo,nombre,descripcion,cantidad,stock,fecha),True
            )
            return 'Equipo created successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)
        
    def deleteEquipo(self,id):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            DELETE FROM logistica.equipo WHERE id = %s;
            """,(id),True
            )
            return 'Equipo deleted successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)
    
    def updateEquipo(self,id,cantidad,stock):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            UPDATE logistica.equipo SET cantidad=%s,stock=%s WHERE id=%s;
            """,(cantidad,stock,id),True
            )
            return 'Equipo updated successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)

if __name__=="__main__":
    equipo_model = EquipoModel()