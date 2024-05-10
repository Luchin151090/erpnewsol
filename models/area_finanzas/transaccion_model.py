from config import PostgresSQLPool, begin
from psycopg2 import DataError, IntegrityError
from flask import request, jsonify
import traceback
import psycopg2.pool

class TransaccionModel:
    def __init__(self):
        self.db_pool = PostgresSQLPool()

    def getTransaccion(self):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            # sql
            query = cursor.execute(
                """SELECT * FROM finanzas.transaccion;"""
            )
            # data
            data = cursor.fetchall()
            datos = list()
            contenido = dict()
            for row in data:
                contenido ={
                    'id':row[0],
                    'fecha_transaccion':row[1],
                    'monto':row[2],
                    'caja_origen':row[3],
                    'caja_destino':row[4]
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

    def createTransaccion(self,fecha_transaccion,monto,caja_origen,caja_destino):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO finanzas.transaccion(fecha_transaccion,monto,caja_origen,caja_destino)
                VALUES(%s,%s,%s,%s);
                """,(fecha_transaccion,monto,caja_origen,caja_destino)
            )
            conn.commit()
            return jsonify({'mensaje': 'Transaccion created successfully'}),201
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

    def deleteTransaccion(self,id):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
            """
            DELETE FROM finanzas.transaccion WHERE id = %s;
            """,(id,)
            )
            conn.commit()
            return jsonify({'mensaje': 'Transaccion delete successfully'}),200
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

    def updateTransaccion(self,id,fecha_transaccion,monto,caja_origen,caja_destino):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
            """
            UPDATE finanzas.transaccion SET fecha_na=%s,saldo_final=%s,saldo_inicial=%s,area_finanzas_id=%s WHERE id=%s;
            """,(fecha_transaccion,monto,caja_origen,caja_destino,id)
            )
            conn.commit()
            return jsonify({'mensaje': 'Transaccion updated successfully'}),200
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
    transaccion = TransaccionModel()