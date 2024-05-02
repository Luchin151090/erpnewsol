from config import PostgresSQLPool
from flask import request
import traceback

class FvalModel:
    def __init__(self):
        self.db_pool = PostgresSQLPool()
      
 #TABLA FVAL
    def getFval(self):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()

            query = cursor.execute(
                """
                SELECT * FROM logistica.fval;
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
                    'cantidad':row[2],
                    'fecha_req':row[3],
                    'solicitante':row[4],
                    'area_solicitante':row[5]
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

    def createFval(self,nombre,cantidad,fecha_req,solicitante,area_solicitante):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            INSERT INTO logistica.fval (nombre,cantidad,fecha_req,solicitante,area_solicitante) VALUES (%s,%s,%s,%s,%s);
            """,(nombre,cantidad,fecha_req,solicitante,area_solicitante),True
            )
            return 'Fval created successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)
        
    def deleteFval(self,nombre):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            DELETE FROM logistica.fval WHERE nombre = %s;
            """,(nombre),True
            )
            return 'Fval deleted successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)
    
    def updateFval(self,cantidad,nombre):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            UPDATE logistica.fval SET cantidad=%s WHERE nombre=%s;
            """,(cantidad,nombre),True
            )
            return 'Fval updated successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)

if __name__=="__main__":
    fval_model = FvalModel()
