from config import PostgresSQLPool, begin
from psycopg2 import DataError, IntegrityError
from flask import request, jsonify
import traceback

class MaterialModel:
    def __init__(self):
        self.db_pool = PostgresSQLPool()

    # TABLA MATERIAL
    def getMaterial(self):
        conn = None
        cursor = None
        try:
            conn = begin()
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

    def createMaterial(self,codigo,nombre,descripcion,cantidad,stock,fecha_ingreso):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
            """
            INSERT INTO logistica.material (codigo,nombre,descripcion,cantidad,stock,fecha_ingreso) VALUES (%s,%s,%s,%s,%s,%s);
            """,(codigo,nombre,descripcion,cantidad,stock,fecha_ingreso)
            )
            conn.commit()
            return jsonify({'mensaje': 'Material created successfully'}),201
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
        
    def deleteMaterial(self,id):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
            """
            DELETE FROM logistica.material WHERE id = %s;
            """,(id,)
            )
            conn.commit()
            return jsonify({'mensaje': 'Material delete successfully'}),200
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
    
    def updateMaterial(self,id,cantidad,stock):
        conn = None
        cursor = None
        try:
            conn = begin()
            cursor = conn.cursor()
            cursor.execute(
            """
            UPDATE cars SET cantidad=%s,stock=%s WHERE id=%s;
            """,(cantidad,stock,id)
            )
            conn.commit()
            return jsonify({'mensaje': 'Material updated successfully'}),200
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
    material_model = MaterialModel()
    