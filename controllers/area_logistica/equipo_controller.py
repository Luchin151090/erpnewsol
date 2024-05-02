from flask import Blueprint,request,jsonify
from flask_cors import CORS,cross_origin


# Importamos el model logistica, su ruta
from models.area_logistica.equipo_model import EquipoModel

# Decorador de endpoint
blue_print = Blueprint('blue_print',__name__)

# Crear un objeto para que nos ayude con la clase
model_equipo = EquipoModel()

@blue_print.route('/equipo',methods=['GET'])
@cross_origin()
def getEquipo():
    content = model_equipo.getEquipo()
    return jsonify(content),200

@blue_print.route('/equipo',method=['POST'])
@cross_origin()
def postEquipo():
    try:
        content = model_equipo.createEquipo(
            request.json['stock'],
            request.json['fecha'],
            request.json['descripcion'],
            request.json['cantidad'],
            request.json['codigo'],
            request.json['nombre']
        )
        return jsonify(content),201
    except Exception as e:
        return jsonify({'error':str(e)}),500

@blue_print.route('/equipo/<int:id>',methods=['DELETE'])
@cross_origin()
def deleteEquipo(id):
    try:
        content = model_equipo.deleteEquipo(id)
        if content:
            return jsonify({'mensaje':'equipo delete successfuly'}),200
        else:
            return jsonify({'error':'no se encontro el ID'}),404
    except Exception as e:
        return jsonify({'error':str(e)}),500

@blue_print.route('/equipo/<int:id>',methods=['PUT'])
@cross_origin()
def putEquipo(id):
    try:
        content = model_equipo.updateEquipo(
            id,
            request.json['cantidad'],
            request.json['stock']
        )
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error':str(e)}),500