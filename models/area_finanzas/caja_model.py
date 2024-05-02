from config import PostgresSQLPool
from flask import request
import traceback

class CajaModel:
    def __init__(self):
        self.db_pool = PostgresSQLPool()

    def getCaja(self):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.getconn()
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
                    'caja_id':row[4]
                }
                datos.append(contenido)
                contenido={}
            return datos
        except Exception as e:
            traceback.print_exc()
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)

    def createCaja(self,nombre_caja,saldo_final,saldo_inicial,caja_id):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO finanzas.caja(nombre_caja,saldo_final,saldo_inicial,caja_id)
                VALUES(%s,%s,%s,%s);
                """,(nombre_caja,saldo_final,saldo_inicial,caja_id),True
            )
            return 'Caja created succesfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)

    def deleteCaja(self,id):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            DELETE FROM finanzas.caja WHERE id = %s;
            """,(id),True
            )
            return 'Caja deleted successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)

    def updateSubarea(self,id,nombre_caja,saldo_final,saldo_inicial,caja_id):
        conn = None
        cursor = None
        try:
            conn = self.db_pool.pool.getconn()
            cursor = conn.cursor()
            cursor.execute(
            """
            UPDATE finanzas.caja SET nombre_caja=%s,saldo_final=%s,saldo_inicial=%s,caja_id=%s WHERE id=%s;
            """,(nombre_caja,saldo_final,saldo_inicial,caja_id,id),True
            )
            return 'Caja updated successfully'
        except Exception as e:
            traceback.print_exc()
            return str(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                self.db_pool.pool.putconn(conn)

if __name__=="__main__":
    pass