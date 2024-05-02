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
    content = model_fval.getFval()
    return jsonify(content),200

@blue_print.route('/fval',methods=['POST'])
@cross_origin()
def postFval():
    content = model_fval.createFval(
        request.json['nombre'],
        request.json['cantidad'],
        request.json['fecha_req'],
        request.json['solicitante'],
        request.json['area_solicitante']
    )
    return jsonify(content),200

@blue_print.route('/fval',methods=['DELETE'])
@cross_origin()
def deleteFval():
    content = model_fval.deleteFval(
        request.json['id']
    )
    return jsonify(content),200

@blue_print.route('/fval',methods=['PUT'])
@cross_origin()
def putFval():
    content = model_fval.updateFval(
        request.json['cantidad'],
        request.json['id']
    )
    return jsonify(content),200