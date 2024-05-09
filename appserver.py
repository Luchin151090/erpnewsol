from flask import Blueprint,Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

# rutas-controller-logistica
from controllers.area_logistica.material_controller import material_blue_print as material
from controllers.area_logistica.almacen_controller import almacen_blue_print as almacen
from controllers.area_logistica.equipo_controller import equipo_blue_print as equipo
from controllers.area_logistica.fval_controller import fval_blue_print as fval
from controllers.area_logistica.subarea_controller import subarea_blue_print as subarea
from controllers.area_logistica.descarga_controller import descarga_blue_print as descarga
from controllers.area_logistica.lotes_controller import lotes_blue_print as lotes
from controllers.area_logistica.producto_controller import producto_blue_print as producto
from controllers.area_logistica.vehiculo_controller import vehiculo_blue_print as vehiculo
# rutas-controller-finanzas
from controllers.area_finanzas.controlasistencia_controller import asistencia_blue_print as asistencia
from controllers.area_finanzas.caja_controller import caja_blue_print as caja
from controllers.area_finanzas.fvac_controller import fvac_blue_print as fvac


# Cargar variables de entorno
load_dotenv()
app = Flask(__name__)

# Registrar los blueprints
app.url_map.strict_slashes=False
##logistica
app.register_blueprint(material,url_prefix='/api')
app.register_blueprint(almacen,url_prefix='/api')
app.register_blueprint(equipo,url_prefix='/api')
app.register_blueprint(fval,url_prefix='/api')
app.register_blueprint(subarea,url_prefix='/api')
app.register_blueprint(descarga,url_prefix='/api')
app.register_blueprint(lotes,url_prefix='/api')
app.register_blueprint(producto,url_prefix='/api')
app.register_blueprint(vehiculo,url_prefix='/api')
##finanzas
app.register_blueprint(caja,url_prefix='/api')
app.register_blueprint(asistencia,url_prefix='/api')
app.register_blueprint(fvac,url_prefix='/api')

# middlewares 
# Más control de los verbos http
CORS(app,methods=["GET","POST","PUT","DELETE"])



if __name__ == "__main__":
    host = os.getenv("HOST")
    port = os.getenv("PORT")

    app.run(host=host,port=port)