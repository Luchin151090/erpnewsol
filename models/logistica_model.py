from config import PostgresSQLPool
from flask import request
import traceback


class LogisticaModel:
    def __init__(self):
        self.db_pool = PostgresSQLPool()

    # TABLA MATERIAL
    def getMaterial(self):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()

            query = cursor.execute(
                """
                SELECT * FROM logistica.material;
                """
            )
            # LISTA PARA RECIBIR LA DATA
            data = cursor.fetchall()

            datos = list()
            
            
            contenido = dict()

            for row in data:
                contenido = {
                    'id':row[0],
                    'codigo':row[1],
                    'nombre':row[2],
                    'descripcion':row[3],
                    'cantidad':row[4],
                    'stock':row[5],
                    'fecha_ingreso':row[6]
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

if __name__=="__main__":
    logistica_model = LogisticaModel()
    
        

