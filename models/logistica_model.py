from config import PostgresSQLPool
from flask import request


class LogisticaModel:
    def __init__(self):
        self.db_pool = PostgresSQLPool()

    # TABLA MATERIAL
    def getMaterial(self):
        query = self.db_pool.execute(
            """
            SELECT * FROM logistica.material;
            """
        )
        # LISTA PARA RECIBIR LA DATA
        data = list()
        contenido = dict()

        for row in query:
            contenido = {
                'id':row[0],
                'codigo':row[1],
                'nombre':row[2],
                'descripcion':row[3],
                'cantidad':row[4],
                'stock':row[5],
                'fecha_ingreso':row[6]
            }
            data.append(contenido)
            contenido={}
        return data

if __name__=="__main__":
    logistica_model = LogisticaModel()
    
        

