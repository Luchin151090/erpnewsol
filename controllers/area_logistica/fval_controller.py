from flask import Blueprint,request,jsonify
from flask_cors import CORS,cross_origin
from psycopg2 import InternalError,Error

# Importamos el model logistica, su ruta
from models.area_logistica.fval_model import FvalModel

# Decorador de endpoint
fval_blue_print = Blueprint('fval_blueprint',__name__)

# Crear un objeto para que nos ayude con la clase
model_fval = FvalModel()

@fval_blue_print.route('/fval',methods=['GET'])
@cross_origin()
def getFval():
    try:
        content = model_fval.getFval()
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error controller':str(e)}),500

@fval_blue_print.route('/fval',methods=['POST'])
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

@fval_blue_print.route('/fval/<int:id>',methods=['DELETE'])
@cross_origin()
def deleteFval(id):
    try:
        content = model_fval.deleteFval(id)
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


@fval_blue_print.route('/fval/<int:id>',methods=['PUT'])
@cross_origin()
def putFval(id):
    try:
        content = model_fval.updateFval(
            request.json['cantidad'],
            id
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