from config import PostgresSQLPool, begin
from psycopg2 import DataError, IntegrityError
from flask import request, jsonify
import traceback
import psycopg2.pool

class CajaModel:
    def __init__(self):
        self.db_pool = PostgresSQLPool()

    def getCaja(self):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            # sql
            query = cursor.execute(
                """SELECT * FROM finanzas.caja;"""
            )
            # data
            data = cursor.fetchall()
            datos = list()
            contenido = dict()
            for row in data:
                contenido ={
                    'id':row[0],
                    'nombre_caja':row[1],
                    'saldo_final':row[2],
                    'saldo_inicial':row[3],
                    'area_finanzas_id':row[4]
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

    def createCaja(self,nombre_caja,saldo_final,saldo_inicial,area_finanzas_id):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO finanzas.caja(nombre_caja,saldo_final,saldo_inicial,area_finanzas_id)
                VALUES(%s,%s,%s,%s);
                """,(nombre_caja,saldo_final,saldo_inicial,area_finanzas_id)
            )
            conn.commit()
            return jsonify({'mensaje': 'Caja created successfully'}),201
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

    def deleteCaja(self,id):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
            """
            DELETE FROM finanzas.caja WHERE id = %s;
            """,(id,)
            )
            conn.commit()
            return jsonify({'mensaje': 'Caja delete successfully'}),200
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

    def updateCaja(self,id,nombre_caja,saldo_final,saldo_inicial,area_finanzas_id):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
            """
            UPDATE finanzas.caja SET nombre_caja=%s,saldo_final=%s,saldo_inicial=%s,area_finanzas_id=%s WHERE id=%s;
            """,(nombre_caja,saldo_final,saldo_inicial,area_finanzas_id,id)
            )
            conn.commit()
            return jsonify({'mensaje': 'Caja updated successfully'}),200
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
    caja = CajaModel()