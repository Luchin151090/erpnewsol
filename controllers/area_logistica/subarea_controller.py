from flask import Blueprint,request,jsonify
from flask_cors import CORS,cross_origin
from psycopg2 import InternalError,Error

# Importamos el model logistica, su ruta
from models.area_logistica.subarea_model import SubareaModel

# Decorador de endpoint
subarea_blue_print = Blueprint('subarea_blueprint',__name__)

# Crear un objeto para que nos ayude con la clase
model_subarea = SubareaModel()

@subarea_blue_print.route('/subarea',methods=['GET'])
@cross_origin()
def getSubarea():
    try:
        content = model_subarea.getSubarea()
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error controller':str(e)}),500

@subarea_blue_print.route('/subarea',methods=['POST'])
@cross_origin()
def postsubarea():
    try:
        content = model_subarea.createSubarea(
            request.json['nombre'],
            request.json['responsable']
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

@subarea_blue_print.route('/subarea/<int:id>',methods=['DELETE'])
@cross_origin()
def deletesubarea(id):
    try:
        content = model_subarea.deleteSubarea(id)
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

@subarea_blue_print.route('/subarea/<int:id>',methods=['PUT'])
@cross_origin()
def putsubarea(id):
    try:
        content = model_subarea.updateSubarea(
            request.json['responsable'],
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