from flask import Blueprint,request,jsonify
from flask_cors import CORS,cross_origin


# Importamos el model logistica, su ruta
from models.area_logistica.material_model import MaterialModel

# Decorador de endpoint
blue_print = Blueprint('blue_print',__name__)

# Crear un objeto para que nos ayude con la clase
model_material = MaterialModel()

@blue_print.route('/material',methods=['GET'])
@cross_origin()
def getMateriales():
    content = model_material.getMaterial()
    return jsonify(content),200