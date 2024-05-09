from flask import Blueprint,request,jsonify
from flask_cors import CORS,cross_origin
from psycopg2 import InternalError,Error

# Importamos el model logistica, su ruta
from models.area_logistica.producto_model import ProductoModel

# Decorador de endpoint
producto_blue_print = Blueprint('producto_blueprint',__name__)

# Crear un objeto para que nos ayude con la clase
model_producto = ProductoModel()

@producto_blue_print.route('/producto',methods=['GET'])
@cross_origin()
def getProducto():
    try:
        content = model_producto.getProducto()
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error controller':str(e)}),500


@producto_blue_print.route('/producto',methods=['POST'])
@cross_origin()
def postProducto():
    try:
        content = model_producto.createProducto(
            request.json['nombre'],
            request.json['descarga_id']
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


@producto_blue_print.route('/producto/<int:id>',methods=['DELETE'])
@cross_origin()
def deleteProducto(id):
    try:
        content = model_producto.deleteProducto(id)
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


@producto_blue_print.route('/producto/<int:id>',methods=['PUT'])
@cross_origin()
def putProducto(id):
    try:
        content = model_producto.updateProducto(
            request.json['nombre'],
            request.json['descarga_id'],
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