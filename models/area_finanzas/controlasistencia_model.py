from config import PostgresSQLPool
from flask import request
import traceback

class ControlAsistenciaModel:
    def __init__(self):
        self.db_pool = PostgresSQLPool()
      
    def getAsistencia(self):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()

            query = cursor.execute(
                """
                SELECT * FROM finanzas.control_asistencia;
                """
            )
            # LISTA PARA RECIBIR LA DATA
            data = cursor.fetchall()
            datos = list()
            contenido = dict()
            for row in data:
                contenido = {
                    'id':row[0],
                    'hora_ingreso':row[1],
                    'hora_salida':row[2],
                    'fecha':row[3],
                    'nombre_empleado':row[4],
                    'cantidad_horas':row[5]
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

    def createAsistencia(self,hora_ingreso,hora_salida,fecha,nombre_empleado,cantidad_horas):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            INSERT INTO finanzas.control_asistencia(hora_ingreso,hora_salida,fecha,nombre_empleado,cantidad_horas)
              VALUES (%s,%s,%s,%s,%s);
            """,(hora_ingreso,hora_salida,fecha,nombre_empleado,cantidad_horas),True
            )
            return 'Asistencia created successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)
        
    def deleteAsistencia(self,id):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            DELETE FROM finanzas.control_asistencia WHERE id = %s;
            """,(id),True
            )
            return 'Asistencia deleted successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)
    
    def updateAsistencia(self,id,hora_ingreso,hora_salida,fecha,nombre_empleado,cantidad_horas):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            UPDATE finanzas.control_asistencia SET 
            hora_ingreso=%s,hora_salida=%s,fecha=%s,nombre_empleado=%s,cantidad_horas=%s WHERE id=%s;
            """,(hora_ingreso,hora_salida,fecha,nombre_empleado,cantidad_horas,id),True
            )
            return 'Asistencia updated successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)

if __name__=="__main__":
    asistencia = ControlAsistenciaModel()