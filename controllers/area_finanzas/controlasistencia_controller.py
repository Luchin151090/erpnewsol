from flask import Blueprint,request,jsonify
from flask_cors import CORS, cross_origin

# Importamos model de asistencia
from models.area_finanzas.controlasistencia_model import ControlAsistenciaModel

# Decorador de endpoint
asistencia_blue_print = Blueprint('asistencia_blueprint',__name__)

#Crear un objeto que nos ayude a traer la data
model_asistencia = ControlAsistenciaModel()

@asistencia_blue_print.route('/asistencia',methods=['GET'])
@cross_origin()
def getAsistencia():
    try:       
        content = model_asistencia.getAsistencia()
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error':str(e)}),500
  

@asistencia_blue_print.route('/asistencia',methods=['POST'])
@cross_origin()
def postAsistencia():
    try:
        content = model_asistencia.createAsistencia(
            request.json['hora_ingreso'],
            request.json['hora_salida'],
            request.json['fecha'],
            request.json['nombre_empleado'],
            request.json['cantidad_horas']
        )
        return jsonify(content),201
    except Exception as e:
        return jsonify({'error':str(e)}),500

@asistencia_blue_print.route('/asistencia/<int:id>',methods=['DELETE'])
@cross_origin()
def deleteAsistencia(id):
    try:
        content = model_asistencia.deleteAsistencia(id)
        if content:
            return jsonify({'mensaje':'asistencia delete successfuly'}),200
        else:
            return jsonify({'error':'no se encontro el ID'}),404
    except Exception as e:
        return jsonify({'error':str(e)}),500
        
    

@asistencia_blue_print.route('/asistencia/<int:id>',methods=['PUT'])
@cross_origin()
def updateAsistencia(id):
    try:
        content = model_asistencia.updateAsistencia(
            request.json['hora_ingreso'],
            request.json['hora_salida'],
            request.json['fecha'],
            request.json['nombre_empleado'],
            request.json['cantidad_horas'] 
        )
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error':str(e)}),500