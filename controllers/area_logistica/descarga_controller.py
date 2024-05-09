from flask import Blueprint,request,jsonify
from flask_cors import CORS,cross_origin
from psycopg2 import InternalError,Error

# Importamos el model logistica, su ruta
from models.area_logistica.descarga_model import DescargaModel

# Decorador de endpoint
descarga_blue_print = Blueprint('descarga_blueprint',__name__)

# Crear un objeto para que nos ayude con la clase
model_descarga = DescargaModel()

@descarga_blue_print.route('/descarga',methods=['GET'])
@cross_origin()
def getDescarga():
    try:
        content = model_descarga.getDescarga()
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error controller':str(e)}),500


@descarga_blue_print.route('/descarga',methods=['POST'])
@cross_origin()
def postDescarga():
    try:
        content = model_descarga.createDescarga(
            request.json['fecha_descarga'],
            request.json['mermas'],
            request.json['vehiculo_id']
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


@descarga_blue_print.route('/descarga/<int:id>',methods=['DELETE'])
@cross_origin()
def deleteDescarga(id):
    try:
        content = model_descarga.deleteDescarga(id)
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


@descarga_blue_print.route('/descarga/<int:id>',methods=['PUT'])
@cross_origin()
def putDescarga(id):
    try:
        content = model_descarga.updateDescarga(
            request.json['mermas'],
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