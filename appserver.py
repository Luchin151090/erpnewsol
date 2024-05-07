from flask import Blueprint,Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

# rutas-controller-logistica
from controllers.area_logistica.material_controller import material_blue_print as material



# rutas-controller-finanzas
from controllers.area_finanzas.controlasistencia_controller import asistencia_blue_print as asistencia
from controllers.area_finanzas.caja_controller import caja_blue_print as caja
from controllers.area_finanzas.fvac_controller import fvac_blue_print as fvac


# Cargar variables de entorno
load_dotenv()
app = Flask(__name__)

# Registrar los blueprints
app.url_map.strict_slashes=False
app.register_blueprint(caja,url_prefix='/api')
app.register_blueprint(material,url_prefix='/api')
app.register_blueprint(asistencia,url_prefix='/api')
app.register_blueprint(fvac,url_prefix='/api')

# middlewares 
# Más control de los verbos http
CORS(app,methods=["GET","POST","PUT","DELETE"])



if __name__ == "__main__":
    host = os.getenv("HOST")
    port = os.getenv("PORT")

    app.run(host=host,port=port)