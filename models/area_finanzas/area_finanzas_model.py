from config import PostgresSQLPool, begin
from psycopg2 import DataError, IntegrityError
from flask import request, jsonify
import traceback
import psycopg2.pool

class FinanzasModel:
    def __init__(self):
        self.db_pool = PostgresSQLPool()

    def getFinanzas(self):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            # sql
            query = cursor.execute(
                """SELECT * FROM area.area_finanzas;"""
            )
            # data
            data = cursor.fetchall()
            datos = list()
            contenido = dict()
            for row in data:
                contenido ={
                    'id':row[0],
                    'nombre':row[1],
                    'area_id':row[2]
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

    def createFinanzas(self,nombre,area_id):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO area.area_finanzas(nombre,area_id)
                VALUES(%s,%s);
                """,(nombre,area_id)
            )
            conn.commit()
            return jsonify({'mensaje': 'Finanzas created successfully'}),201
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

    def deleteFinanzas(self,id):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
            """
            DELETE FROM area.area_finanzas WHERE id = %s;
            """,(id,)
            )
            conn.commit()
            return jsonify({'mensaje': 'Finanzas delete successfully'}),200
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

    def updateFinanzas(self,id,nombre,area_id):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
            """
            UPDATE finanzas.caja SET nombre =%s, area_id=%s WHERE id=%s;
            """,(nombre,area_id,id)
            )
            conn.commit()
            return jsonify({'mensaje': 'Finanzas updated successfully'}),200
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
    finanza = FinanzasModel()