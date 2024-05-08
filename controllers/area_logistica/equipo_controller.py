from flask import Blueprint,request,jsonify
from flask_cors import CORS,cross_origin
from psycopg2 import InternalError,Error

# Importamos el model logistica, su ruta
from models.area_logistica.equipo_model import EquipoModel

# Decorador de endpoint
equipo_blue_print = Blueprint('equipo_blueprint',__name__)

# Crear un objeto para que nos ayude con la clase
model_equipo = EquipoModel()

@equipo_blue_print.route('/equipo',methods=['GET'])
@cross_origin()
def getEquipo():
    try:
        content = model_equipo.getEquipo()
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error controller':str(e)}),500

@equipo_blue_print.route('/equipo',methods=['POST'])
@cross_origin()
def postEquipo():
    try:
        content = model_equipo.createEquipo(
            request.json['stock'],
            request.json['fecha'],
            request.json['descripcion'],
            request.json['cantidad'],
            request.json['codigo'],
            request.json['nombre']
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

@equipo_blue_print.route('/equipo/<int:id>',methods=['DELETE'])
@cross_origin()
def deleteEquipo(id):
    try:
        content = model_equipo.deleteEquipo(id)
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

@equipo_blue_print.route('/equipo/<int:id>',methods=['PUT'])
@cross_origin()
def putEquipo(id):
    try:
        content = model_equipo.updateEquipo(
            id,
            request.json['cantidad'],
            request.json['stock']
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