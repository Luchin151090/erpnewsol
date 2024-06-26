from config import PostgresSQLPool, begin
from psycopg2 import DataError, IntegrityError
from flask import request, jsonify
import traceback

class EquipoModel:
    def __init__(self):
        self.db_pool = PostgresSQLPool()
        
        # TABLA EQUIPO
    
    def getEquipo(self):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()

            query = cursor.execute(
                """
                SELECT * FROM logistica.equipo_herramienta;
                """
            )
            # LISTA PARA RECIBIR LA DATA
            data = cursor.fetchall()

            datos = list()
            
            
            contenido = dict()

            for row in data:
                contenido = {
                    'id':row[0],
                    'stock':row[1],
                    'fecha':row[2],
                    'descripcion':row[3],
                    'cantidad':row[4],
                    'codigo':row[5],
                    'nombre':row[6],
                    'almacen_id':row[7]
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

    def createEquipo(self,stock,fecha,descripcion,cantidad,codigo,nombre,almacen_id):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
            """
            INSERT INTO logistica.equipo_herramienta (stock,fecha,descripcion,cantidad,codigo,nombre,almacen_id) VALUES (%s,%s,%s,%s,%s,%s,%s);
            """,(stock,fecha,descripcion,cantidad,codigo,nombre,almacen_id)
            )
            conn.commit()
            return jsonify({'mensaje': 'Equipo created successfully'}),201
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
        
    def deleteEquipo(self,id):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
            """
            DELETE FROM logistica.equipo_herramienta WHERE id = %s;
            """,(id,)
            )
            conn.commit()
            return jsonify({'mensaje': 'Equipo delete successfully'}),200
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
    
    def updateEquipo(self,id,cantidad,stock,almacen_id):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
            """
            UPDATE logistica.equipo_herramienta SET cantidad=%s,stock=%s,almacen_id=%s WHERE id=%s;
            """,(cantidad,stock,almacen_id,id)
            )
            conn.commit()
            return jsonify({'mensaje': 'Equipo updated successfully'}),200
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
    equipo_model = EquipoModel()