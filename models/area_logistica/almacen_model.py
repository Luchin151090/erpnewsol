from config import PostgresSQLPool
from flask import request
import traceback

class AlmacenModel:
    def __init__(self):
        self.db_pool = PostgresSQLPool()
    
    def getAlmacen(self):
        pass

    def createAlmacen(self):
        pass

    def deleteAlmacen(self):
        pass

    def updateAlmacen(self):
        pass

if __name__=="__main__":
    almacen_model = AlmacenModel()