from flask import Blueprint,request,jsonify
from flask_cors import CORS, cross_origin

# Importamos model de asistencia
from models.area_finanzas.caja_model import CajaModel

# Decorador de endpoint
blue_print = Blueprint('blue_print',__name__)

#Crear un objeto que nos ayude a traer la data
model_caja = CajaModel()

@blue_print.route('/caja',methods=['GET'])
@cross_origin()
def getCaja():
    try:       
        content = model_caja.getCaja()
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error':str(e)}),500
  

@blue_print.route('/caja',methods=['POST'])
@cross_origin()
def postCaja():
    try:
        content = model_caja.createCaja(
            request.json['nombre_caja'],
            request.json['saldo_final'],
            request.json['saldo_inicial'],
            request.json['caja_id']
        )
        return jsonify(content),201
    except Exception as e:
        return jsonify({'error':str(e)}),500

@blue_print.route('/caja/<int:id>',methods=['DELETE'])
@cross_origin()
def deleteCaja(id):
    try:
        content = model_caja.deleteCaja(id)
        if content:
            return jsonify({'mensaje':'caja delete successfuly'}),200
        else:
            return jsonify({'error':'no se encontro el ID'}),404
    except Exception as e:
        return jsonify({'error':str(e)}),500
        
    

@blue_print.route('/caja/<int:id>',methods=['PUT'])
@cross_origin()
def updateCaja(id):
    try:
        content = model_caja.updateCaja(
            request.json['nombre_caja'],
            request.json['saldo_final'],
            request.json['saldo_inicial'],
            request.json['caja_id'] 
        )
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error':str(e)}),500