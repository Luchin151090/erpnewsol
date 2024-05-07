from flask import Blueprint,request,jsonify
from flask_cors import CORS, cross_origin


# Importamos model de asistencia
from models.area_finanzas.fvac_model import FvacModel

# Decorador de endpoint
fvac_blue_print = Blueprint('fvac_blueprint',__name__)

#Crear un objeto que nos ayude a traer la data
model_fvac = FvacModel()

@fvac_blue_print.route('/fvac',methods=['GET'])
@cross_origin()
def getCaja():
    try:       
        content = model_fvac.getReporte()
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error':str(e)}),500
  

@fvac_blue_print.route('/fvac',methods=['POST'])
@cross_origin()
def postCaja():
    try:
        content = model_fvac.createReporte(
            request.json['monto_ingreso'],
            request.json['monto_salida'],
            request.json['fecha']
        )
        return jsonify(content),201
    except Exception as e:
        return jsonify({'error':str(e)}),500

@fvac_blue_print.route('/fvac/<int:id>',methods=['DELETE'])
@cross_origin()
def deleteCaja(id):
    try:
        content = model_fvac.deleteReporte(id)
        if content:
            return jsonify({'mensaje':'fvac delete successfuly'}),200
        else:
            return jsonify({'error':'no se encontro el ID'}),404
    except Exception as e:
        return jsonify({'error':str(e)}),500
        
    

@fvac_blue_print.route('/fvac/<int:id>',methods=['PUT'])
@cross_origin()
def updateCaja(id):
    try:
        content = model_fvac.updateReporte(
            request.json['monto_ingreso'],
            request.json['monto_salida'],
            request.json['fecha']
        )
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error':str(e)}),500