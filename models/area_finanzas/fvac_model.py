from config import PostgresSQLPool
from flask import request
import traceback

class FvacModel:
    def __init__(self):
        self.db_pool = PostgresSQLPool()
      
    def getReporte(self):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()

            query = cursor.execute(
                """
                SELECT * FROM finanzas.fvac;
                """
            )
            # LISTA PARA RECIBIR LA DATA
            data = cursor.fetchall()
            datos = list()
            contenido = dict()
            for row in data:
                contenido = {
                    'id':row[0],
                    'monto_ingreso':row[1],
                    'monto_salida':row[2],
                    'fecha':row[3],
                   
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

    def createReporte(self,monto_ingreso,monto_salida,fecha):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            INSERT INTO finanzas.fvac
            (monto_ingreso,monto_salida,fecha)
              VALUES (%s,%s,%s);
            """,(monto_ingreso,monto_salida,fecha),True
            )
            return 'Reporte created successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)
        
    def deleteReporte(self,id):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            DELETE FROM finanzas.fvac WHERE id = %s;
            """,(id),True
            )
            return 'Reporte deleted successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)
    
    def updateReporte(self,id,monto_ingreso,monto_salida,fecha):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            UPDATE finanzas.fvac SET 
            monto_ingreso=%s,monto_salida=%s,fecha=%s WHERE id=%s;
            """,(monto_ingreso,monto_salida,fecha,id),True
            )
            return 'Reporte updated successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)

if __name__=="__main__":
    reporte_model = FvacModel()