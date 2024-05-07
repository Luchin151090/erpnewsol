from config import PostgresSQLPool
from flask import request
import traceback

class MaterialModel:
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

    def createMaterial(self,codigo,nombre,descripcion,cantidad,stock,fecha_ingreso):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            INSERT INTO logistica.material (codigo,nombre,descripcion,cantidad,stock,fecha_ingreso) VALUES (%s,%s,%s,%s,%s,%s);
            """,(codigo,nombre,descripcion,cantidad,stock,fecha_ingreso),True
            )
            
            return 'Material created successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)
        
    def deleteMaterial(self,codigo):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            DELETE FROM logistica.material WHERE codigo = %s;
            """,(codigo),True
            )
            return 'Material deleted successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)
    
    def updateMaterial(self,codigo,cantidad,stock):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            UPDATE cars SET cantidad=%s,stock=%s WHERE codigo=%s;
            """,(cantidad,stock,codigo),True
            )
            return 'Material updated successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)


if __name__=="__main__":
    material_model = MaterialModel()
    