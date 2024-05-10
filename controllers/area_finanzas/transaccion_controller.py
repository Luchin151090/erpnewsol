from flask import Blueprint,request,jsonify
from flask_cors import CORS, cross_origin
from psycopg2 import InternalError,Error

# Importamos model de asistencia
from models.area_finanzas.transaccion_model import TransaccionModel

# Decorador de endpoint
transaccion_blue_print = Blueprint('transaccion_blueprint',__name__)

#Crear un objeto que nos ayude a traer la data
model_transaccion = TransaccionModel()

@transaccion_blue_print.route('/transaccion',methods=['GET'])
@cross_origin()
def getFvac():
    try:       
        content = model_transaccion.getTransaccion()
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error controller':str(e)}),500
  

@transaccion_blue_print.route('/transaccion',methods=['POST'])
@cross_origin()
def postFvac():
    try:
        content = model_transaccion.createTransaccion(
            request.json['fecha_transaccion'],
            request.json['monto'],
            request.json['caja_origen'],
            request.json['caja_destino']
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

@transaccion_blue_print.route('/transaccion/<int:id>',methods=['DELETE'])
@cross_origin()
def deleteFvac(id):
    try:
        content = model_transaccion.deleteTransaccion(id)
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
        
    

@transaccion_blue_print.route('/transaccion/<int:id>',methods=['PUT'])
@cross_origin()
def updateFvac(id):
    try:
        content = model_transaccion.updateTransaccion(
            id,
            request.json['fecha_transaccion'],
            request.json['monto'],
            request.json['caja_origen'],
            request.json['caja_destino']
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