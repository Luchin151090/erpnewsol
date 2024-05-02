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
    content = model_material.getMaterial()
    return jsonify(content),200

@material_blue_print.route('/material',methods=['POST'])
@cross_origin()
def postMateriales():
    content = model_material.createMaterial(
        request.json['codigo'],
        request.json['nombre'],
        request.json['descripcion'],
        request.json['cantidad'],
        request.json['stock'],
        request.json['fecha_ingreso']
    )
    return jsonify(content),200

@material_blue_print.route('/material',methods=['DELETE'])
@cross_origin()
def deleteMateriales():
    content = model_material.deleteMaterial(
        request.json['codigo']
    )
    return jsonify(content),200

@material_blue_print.route('/material',methods=['PUT'])
@cross_origin()
def putMateriales():
    content = model_material.updateMaterial(
        request.json['codigo'],
        request.json['cantidad'],
        request.json['stock']
    )
    return jsonify(content),200