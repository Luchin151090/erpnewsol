from flask import Blueprint,request,jsonify
from flask_cors import CORS,cross_origin


# Importamos el model logistica, su ruta
from models.area_logistica.fval_model import FvalModel

# Decorador de endpoint
blue_print = Blueprint('blue_print',__name__)

# Crear un objeto para que nos ayude con la clase
model_fval = FvalModel()

@blue_print.route('/fval',methods=['GET'])
@cross_origin()
def getFval():
    try:
        content = model_fval.getFval()
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error':str(e)}),500

@blue_print.route('/fval',methods=['POST'])
@cross_origin()
def postFval():
    try:
        content = model_fval.createFval(
            request.json['nombre'],
            request.json['cantidad'],
            request.json['fecha_req'],
            request.json['solicitante'],
            request.json['area_solicitante']
        )
        return jsonify(content),201
    except Exception as e:
        return jsonify({'error':str(e)}),500

@blue_print.route('/fval/<int:id>',methods=['DELETE'])
@cross_origin()
def deleteFval(id):
    try:
        content = model_fval.deleteFval(id)
        if content:
            return jsonify({'mensaje':'fval delete successfuly'}),200
        else:
            return jsonify({'error':'no se encontro el ID'}),404
    except Exception as e:
        return jsonify({'error':str(e)}),500


@blue_print.route('/fval/<int:id>',methods=['PUT'])
@cross_origin()
def putFval(id):
    try:
        content = model_fval.updateFval(
            request.json['cantidad'],
            id
        )
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error':str(e)}),500