from flask import Blueprint,Flask
from flask_cors import CORS
from dotenv import load_dotenv
from controllers.area_logistica.almacen_controller import blue_print as almacen
from controllers.area_logistica.equipo_controller import blue_print as equipo
from controllers.area_logistica.fval_controller import blue_print as fval
from controllers.area_logistica.material_controller import blue_print as material
from controllers.area_logistica.subarea_controller import blue_print as subarea
import os

# Cargar variables de entorno
load_dotenv()
app = Flask(__name__)

# Registrar los blueprints
app.url_map.strict_slashes=False
app.register_blueprint(almacen,url_prefix='/almacen')
app.register_blueprint(almacen,url_prefix='/almacen')
app.register_blueprint(almacen,url_prefix='/almacen')
app.register_blueprint(almacen,url_prefix='/almacen')
app.register_blueprint(equipo,url_prefix='/equipo')
app.register_blueprint(fval,url_prefix='/fval')
app.register_blueprint(material,url_prefix='/material')
app.register_blueprint(subarea,url_prefix='/subarea')

# middlewares 
# Más control de los verbos http
CORS(app,methods=["GET","POST","PUT","DELETE"])



if __name__ == "__main__":
    host = os.getenv("HOST")
    port = os.getenv("PORT")

    app.run(host=host,port=port)