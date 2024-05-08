from flask import Blueprint,request,jsonify
from flask_cors import CORS, cross_origin
from psycopg2 import InternalError,Error
# Importamos model de asistencia
from models.area_finanzas.caja_model import CajaModel

# Decorador de endpoint
caja_blue_print = Blueprint('caja_blueprint',__name__)

#Crear un objeto que nos ayude a traer la data
model_caja = CajaModel()

@caja_blue_print.route('/caja',methods=['GET'])
@cross_origin()
def getCaja():
    try:       
        content = model_caja.getCaja()
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error controller':str(e)}),500
  

@caja_blue_print.route('/caja',methods=['POST'])
@cross_origin()
def postCaja():
    try:
        content = model_caja.createCaja(
            request.json['nombre_caja'],
            request.json['saldo_final'],
            request.json['saldo_inicial'],
            request.json['caja_id']
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

@caja_blue_print.route('/caja/<int:id>',methods=['DELETE'])
@cross_origin()
def deleteCaja(id):
    try:
        content = model_caja.deleteCaja(id)
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
        
    

@caja_blue_print.route('/caja/<int:id>',methods=['PUT'])
@cross_origin()
def updateCaja(id):
    try:
        content = model_caja.updateCaja(
            id,
            request.json['nombre_caja'],
            request.json['saldo_final'],
            request.json['saldo_inicial'],
            request.json['caja_id'] 
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