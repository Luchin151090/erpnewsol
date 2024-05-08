from flask import Blueprint,request,jsonify
from flask_cors import CORS,cross_origin
from psycopg2 import InternalError,Error

# Importamos el model logistica, su ruta
from models.area_logistica.almacen_model import AlmacenModel

# Decorador de endpoint
almacen_blue_print = Blueprint('almacen_blueprint',__name__)

# Crear un objeto para que nos ayude con la clase
model_almacen = AlmacenModel()

@almacen_blue_print.route('/almacen',methods=['GET'])
@cross_origin()
def getAlmacen():
    try:
        content = model_almacen.getAlmacen()
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error controller':str(e)}),500


@almacen_blue_print.route('/almacen',methods=['POST'])
@cross_origin()
def postAlmacen():
    try:
        content = model_almacen.createAlmacen(
            request.json['nombre'],
            request.json['ubicacion']
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


@almacen_blue_print.route('/almacen/<int:id>',methods=['DELETE'])
@cross_origin()
def deleteAlmacen(id):
    try:
        content = model_almacen.deleteAlmacen(id)
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


@almacen_blue_print.route('/almacen/<int:id>',methods=['PUT'])
@cross_origin()
def putAlmacen(id):
    try:
        content = model_almacen.updateAlmacen(
            request.json['nombre'],
            request.json['ubicacion'],
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