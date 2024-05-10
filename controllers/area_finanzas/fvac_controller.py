from flask import Blueprint,request,jsonify
from flask_cors import CORS, cross_origin
from psycopg2 import InternalError,Error

# Importamos model de asistencia
from models.area_finanzas.fvac_model import FvacModel

# Decorador de endpoint
fvac_blue_print = Blueprint('fvac_blueprint',__name__)

#Crear un objeto que nos ayude a traer la data
model_fvac = FvacModel()

@fvac_blue_print.route('/fvac',methods=['GET'])
@cross_origin()
def getFvac():
    try:       
        content = model_fvac.getReporte()
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error controller':str(e)}),500
  

@fvac_blue_print.route('/fvac',methods=['POST'])
@cross_origin()
def postFvac():
    try:
        content = model_fvac.createReporte(
            request.json['monto_ingreso'],
            request.json['monto_salida'],
            request.json['fecha'],
            request.json['area_finanzas_id']
        )
        if content:
            return content
        else:
            return jsonify({'error': 'No se pudo crear'}), 500
    except InternalError as e:
        return jsonify({'error': 'InternalError: ' + str(e)}), 500
    except Error as e:
        return jsonify({'error':'error basse de datos '+str(e)}),500
    except Exception as e:
        return jsonify({'error controller': str(e)}), 500

@fvac_blue_print.route('/fvac/<int:id>',methods=['DELETE'])
@cross_origin()
def deleteFvac(id):
    try:
        content = model_fvac.deleteReporte(id)
        if content:
            return content
        else:
            return jsonify({'error': 'no se encontro el ID'}), 500
    except InternalError as e:
        return jsonify({'error': 'InternalError: ' + str(e)}), 500
    except Error as e:
        return jsonify({'error':'error basse de datos '+str(e)}),500
    except Exception as e:
        return jsonify({'error controller': str(e)}), 500
        
    

@fvac_blue_print.route('/fvac/<int:id>',methods=['PUT'])
@cross_origin()
def updateFvac(id):
    try:
        content = model_fvac.updateReporte(
            id,
            request.json['monto_ingreso'],
            request.json['monto_salida'],
            request.json['fecha'],
            request.json['area_finanzas_id']
        )
        if content:
            return content
        else:
            return jsonify({'error': 'no se encontro el ID'}), 500
    except InternalError as e:
        return jsonify({'error': 'InternalError: ' + str(e)}), 500
    except Error as e:
        return jsonify({'error':'error basse de datos '+str(e)}),500
    except Exception as e:
        return jsonify({'error controller': str(e)}), 500