from flask import Blueprint,request,jsonify
from flask_cors import CORS,cross_origin


# Importamos el model logistica, su ruta
from models.area_logistica.subarea_model import SubareaModel

# Decorador de endpoint
blue_print = Blueprint('blue_print',__name__)

# Crear un objeto para que nos ayude con la clase
model_subarea = SubareaModel()

@blue_print.route('/subarea',methods=['GET'])
@cross_origin()
def getSubarea():
    content = model_subarea.getSubarea()
    return jsonify(content),200

@blue_print.route('/subarea',method=['POST'])
@cross_origin()
def postsubarea():
    content = model_subarea.createSubarea(
        request.json['nombre'],
        request.json['responsable']
    )
    return jsonify(content),200

@blue_print.route('/subarea',methods=['DELETE'])
@cross_origin()
def deletesubarea():
    content = model_subarea.deleteSubarea(
        request.json['id']
    )
    return jsonify(content),200

@blue_print.route('/subarea',methods=['PUT'])
@cross_origin()
def putsubarea():
    content = model_subarea.updateSubarea(
        request.json['responsable'],
        request.json['id']
    )
    return jsonify(content),200