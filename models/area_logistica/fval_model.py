from config import PostgresSQLPool, begin
from psycopg2 import DataError, IntegrityError
from flask import request, jsonify
import traceback

class FvalModel:
    def __init__(self):
        self.db_pool = PostgresSQLPool()
      
 #TABLA FVAL
    def getFval(self):
        conn = None
        cursor = None
        try:
            conn = begin()
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
            conn.commit()
            return datos
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def createFval(self,nombre,cantidad,fecha_req,solicitante,area_solicitante):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
            """
            INSERT INTO logistica.fval (nombre,cantidad,fecha_req,solicitante,area_solicitante) VALUES (%s,%s,%s,%s,%s);
            """,(nombre,cantidad,fecha_req,solicitante,area_solicitante)
            )
            conn.commit()
            return jsonify({'mensaje': 'Fval created successfully'}),201
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
        
    def deleteFval(self,id):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
            """
            DELETE FROM logistica.fval WHERE id = %s;
            """,(id,)
            )
            conn.commit()
            return jsonify({'mensaje': 'Fval delete successfully'}),200
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
    
    def updateFval(self,cantidad,id):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
            """
            UPDATE logistica.fval SET cantidad=%s WHERE id=%s;
            """,(cantidad,id)
            )
            conn.commit()
            return jsonify({'mensaje': 'Fval updated successfully'}),200
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
    fval_model = FvalModel()
