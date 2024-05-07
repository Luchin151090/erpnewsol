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
    try:
        content = model_subarea.getSubarea()
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error':str(e)}),500

@blue_print.route('/subarea',methods=['POST'])
@cross_origin()
def postsubarea():
    try:
        content = model_subarea.createSubarea(
            request.json['nombre'],
            request.json['responsable']
        )
        return jsonify(content),201
    except Exception as e:
        return jsonify({'error':str(e)}),500

@blue_print.route('/subarea/<int:id>',methods=['DELETE'])
@cross_origin()
def deletesubarea(id):
    try:
        content = model_subarea.deleteSubarea(id)
        if content:
            return jsonify({'mensaje':'subarea delete successfuly'}),200
        else:
            return jsonify({'error':'no se encontro el ID'}),404
    except Exception as e:
        return jsonify({'error':str(e)}),500

@blue_print.route('/subarea/<int:id>',methods=['PUT'])
@cross_origin()
def putsubarea(id):
    try:
        content = model_subarea.updateSubarea(
            request.json['responsable'],
            id
        )        
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error':str(e)}),500