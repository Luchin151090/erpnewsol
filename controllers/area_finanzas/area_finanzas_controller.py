from flask import Blueprint,request,jsonify
from flask_cors import CORS, cross_origin
from psycopg2 import InternalError,Error
# Importamos model de asistencia

from models.area_finanzas.area_finanzas_model import FinanzasModel
# Decorador de endpoint
caja_blue_print = Blueprint('caja_blueprint',__name__)

#Crear un objeto que nos ayude a traer la data
model_finanzas = FinanzasModel()

@caja_blue_print.route('/finanzas',methods=['GET'])
@cross_origin()
def getFinanza():
    try:       
        content = model_finanzas.getFinanzas()
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error controller':str(e)}),500
  

@caja_blue_print.route('/finanzas',methods=['POST'])
@cross_origin()
def postFinanza():
    try:
        content = model_finanzas.createFinanzas(
            request.json['nombre'],
            request.json['area_id']
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

@caja_blue_print.route('/finanzas/<int:id>',methods=['DELETE'])
@cross_origin()
def deleteFinanza(id):
    try:
        content = model_finanzas.deleteFinanzas(id)
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
        
    

@caja_blue_print.route('/finanzas/<int:id>',methods=['PUT'])
@cross_origin()
def updateFinanza(id):
    try:
        content = model_finanzas.updateFinanzas(
            id,
            request.json['nombre'],
            request.json['area_id']
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