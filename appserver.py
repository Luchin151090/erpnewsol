from flask import Blueprint,Flask
from flask_cors import CORS
from dotenv import load_dotenv
from controllers.area_logistica.logistica_controller import blue_print
import os

# rutas-controller-logistica
from controllers.area_logistica.material_controller import blue_print as material



# rutas-controller-finanzas
from controllers.area_finanzas.controlasistencia_controller import blue_print as asistencia



# Cargar variables de entorno
load_dotenv()
app = Flask(__name__)

# Registrar los blueprints
app.url_map.strict_slashes=False
app.register_blueprint(blue_print,url_prefix='/api')

# middlewares 
# Más control de los verbos http
CORS(app,methods=["GET","POST","PUT","DELETE"])



if __name__ == "__main__":
    host = os.getenv("HOST")
    port = os.getenv("PORT")

    app.run(host=host,port=port)