from flask import Blueprint,request,jsonify
from flask_cors import CORS,cross_origin
from psycopg2 import InternalError,Error

# Importamos el model logistica, su ruta
from models.area_logistica.lotes_model import LotesModel

# Decorador de endpoint
lotes_blue_print = Blueprint('lotes_blueprint',__name__)

# Crear un objeto para que nos ayude con la clase
model_lotes = LotesModel()

@lotes_blue_print.route('/lotes',methods=['GET'])
@cross_origin()
def getLotes():
    try:
        content = model_lotes.getLotes()
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error controller':str(e)}),500


@lotes_blue_print.route('/lotes',methods=['POST'])
@cross_origin()
def postLotes():
    try:
        content = model_lotes.createLotes(
            request.json['cantidad'],
            request.json['fecha_vencimiento'],
            request.json['fecha_produccion'],
            request.json['hora_produccion'],
            request.json['almacen_id'],
            request.json['producto_id']
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


@lotes_blue_print.route('/lotes/<int:id>',methods=['DELETE'])
@cross_origin()
def deleteLotes(id):
    try:
        content = model_lotes.deleteLotes(id)
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


@lotes_blue_print.route('/lotes/<int:id>',methods=['PUT'])
@cross_origin()
def putLotes(id):
    try:
        content = model_lotes.updateLotes(
            request.json['nombre'],
            request.json['ubicacion'],
            request.json['area_logistica_id'],
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