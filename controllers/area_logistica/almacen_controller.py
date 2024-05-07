from flask import Blueprint,request,jsonify
from flask_cors import CORS,cross_origin


# Importamos el model logistica, su ruta
from models.area_logistica.almacen_model import AlmacenModel

# Decorador de endpoint
blue_print = Blueprint('blue_print',__name__)

# Crear un objeto para que nos ayude con la clase
model_almacen = AlmacenModel()

@blue_print.route('/almacen',methods=['GET'])
@cross_origin()
def getAlmacen():
    try:
        content = model_almacen.getAlmacen()
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error':str(e)}),500


@blue_print.route('/almacen',methods=['POST'])
@cross_origin()
def postAlmacen():
    try:
        content = model_almacen.createAlmacen(
            request.json['nombre'],
            request.json['ubicacion']
        )
        return jsonify(content),201
    except Exception as e:
        return jsonify({'error':str(e)}),500


@blue_print.route('/almacen/<int:id>',methods=['DELETE'])
@cross_origin()
def deleteAlmacen(id):
    try:
        content = model_almacen.deleteAlmacen(id)
        if content:
            return jsonify({'mensaje':'almacen delete successfuly'}),200
        else:
            return jsonify({'error':'no se encontro el ID'}),404
    except Exception as e:
        return jsonify({'error':str(e)}),500


@blue_print.route('/almacen/<int:id>',methods=['PUT'])
@cross_origin()
def putAlmacen(id):
    try:
        content = model_almacen.updateAlmacen(
            request.json['nombre'],
            request.json['ubicacion'],
            id
        )
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error':str(e)}),500