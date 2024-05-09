from flask import Blueprint,request,jsonify
from flask_cors import CORS,cross_origin
from psycopg2 import InternalError,Error

# Importamos el model logistica, su ruta
from models.area_logistica.vehiculo_model import VehiculoModel

# Decorador de endpoint
vehiculo_blue_print = Blueprint('vehiculo_blueprint',__name__)

# Crear un objeto para que nos ayude con la clase
model_vehiculo = VehiculoModel()

@vehiculo_blue_print.route('/vehiculo',methods=['GET'])
@cross_origin()
def getVehiculo():
    try:
        content = model_vehiculo.getVehiculo()
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error controller':str(e)}),500


@vehiculo_blue_print.route('/vehiculo',methods=['POST'])
@cross_origin()
def postVehiculo():
    try:
        content = model_vehiculo.createVehiculo(
            request.json['nombre'],
            request.json['capacidad'],
            request.json['carga_neta']
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


@vehiculo_blue_print.route('/vehiculo/<int:id>',methods=['DELETE'])
@cross_origin()
def deleteVehiculo(id):
    try:
        content = model_vehiculo.deleteVehiculo(id)
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


@vehiculo_blue_print.route('/vehiculo/<int:id>',methods=['PUT'])
@cross_origin()
def putVehiculo(id):
    try:
        content = model_vehiculo.updateVehiculo(
            request.json['carga_neta'],
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