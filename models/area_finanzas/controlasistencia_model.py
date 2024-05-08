from psycopg2 import DataError, IntegrityError
from config import PostgresSQLPool,begin
from flask import request,jsonify
import traceback

class ControlAsistenciaModel:
    def __init__(self):
        self.db_pool = PostgresSQLPool()
      
    def getAsistencia(self):
        conn = None
        cursor = None
        try:
            conn = begin()
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
                    'hora_ingreso':row[1].strftime('%H:%M:%S'),
                    'hora_salida':row[2].strftime('%H:%M:%S'),
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
                conn.close()

    def createAsistencia(self,hora_ingreso,hora_salida,fecha,nombre_empleado,cantidad_horas):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
            """
            INSERT INTO finanzas.control_asistencia(hora_ingreso,hora_salida,fecha,nombre_empleado,cantidad_horas)
              VALUES (%s,%s,%s,%s,%s);
            """,(hora_ingreso,hora_salida,fecha,nombre_empleado,cantidad_horas)
            )
            conn.commit()
            return jsonify({'mensaje': 'Asistencia created successfully'}),201
        except DataError as e:  # Captura específicamente el error de tipo de dato incorrecto
            traceback.print_exc()
            return jsonify({'error': 'DataError: ' + str(e)}),400
        except IntegrityError as e:
            traceback.print_exc()
            return jsonify({'error': 'IntegrityError: ' + str(e)}), 400
        except Exception as e:
            traceback.print_exc()
            return jsonify({'error model': str(e)}), 500
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        
    def deleteAsistencia(self,id):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
            """
            DELETE FROM finanzas.control_asistencia WHERE id = %s;
            """,(id,)
            )
            conn.commit()
            return jsonify({'mensaje': 'Asistencia delete successfully'}),200
        except DataError as e:  # Captura específicamente el error de tipo de dato incorrecto
            traceback.print_exc()
            return jsonify({'error': 'DataError: ' + str(e)}),400
        except IntegrityError as e:
            traceback.print_exc()
            return jsonify({'error': 'IntegrityError: ' + str(e)}), 400
        except Exception as e:
            traceback.print_exc()
            return jsonify({'error model': str(e)}), 500
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
    
    def updateAsistencia(self,id,hora_ingreso,hora_salida,fecha,nombre_empleado,cantidad_horas):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
            """
            UPDATE finanzas.control_asistencia SET 
            hora_ingreso=%s,hora_salida=%s,fecha=%s,nombre_empleado=%s,cantidad_horas=%s WHERE id=%s;
            """,(hora_ingreso,hora_salida,fecha,nombre_empleado,cantidad_horas,id)
            )
            conn.commit()
            return jsonify({'mensaje': 'Asistencia updated successfully'}),200
        except DataError as e:  # Captura específicamente el error de tipo de dato incorrecto
            traceback.print_exc()
            return jsonify({'error': 'DataError: ' + str(e)}),400
        except IntegrityError as e:
            traceback.print_exc()
            return jsonify({'error': 'IntegrityError: ' + str(e)}), 400
        except Exception as e:
            traceback.print_exc()
            return jsonify({'error model': str(e)}), 500
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

if __name__=="__main__":
    asistencia = ControlAsistenciaModel()