from flask import Blueprint,request,jsonify
from flask_cors import CORS,cross_origin


# Importamos el model logistica, su ruta
from models.area_logistica.material_model import MaterialModel

# Decorador de endpoint
material_blue_print = Blueprint('material_blueprint',__name__)

# Crear un objeto para que nos ayude con la clase
model_material = MaterialModel()

@material_blue_print.route('/material',methods=['GET'])
@cross_origin()
def getMateriales():
    try:
        content = model_material.getMaterial()
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error':str(e)}),500

@material_blue_print.route('/material',methods=['POST'])
@cross_origin()
def postMateriales():
    try:
        content = model_material.createMaterial(
            request.json['codigo'],
            request.json['nombre'],
            request.json['descripcion'],
            request.json['cantidad'],
            request.json['stock'],
            request.json['fecha_ingreso']
        )
        return jsonify(content),201
    except Exception as e:
        return jsonify({'error':str(e)}),500

@material_blue_print.route('/material/<int:id>',methods=['DELETE'])
@cross_origin()
def deleteMateriales(id):
    try:
        content = model_material.deleteMaterial(id)
        if content:
            return jsonify({'mensaje':'material delete successfuly'}),200
        else:
            return jsonify({'error':'no se encontro el ID'}),404
    except Exception as e:
        return jsonify({'error':str(e)}),500

@material_blue_print.route('/material/<int:id>',methods=['PUT'])
@cross_origin()
def putMateriales(id):
    try:
        content = model_material.updateMaterial(
            id,
            request.json['cantidad'],
            request.json['stock']
        )
        return jsonify(content),200
    except Exception as e:
        return jsonify({'error':str(e)}),500