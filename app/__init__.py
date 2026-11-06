from flask import Flask, jsonify
from app.routes.parqueadero_routes import parqueadero_bp

def create_app():
    app = Flask(__name__)

    # Ruta para la página principal
    @app.route('/')
    def index():
        return jsonify({
            "estado": "Servidor Activo",
            "mensaje": "Bienvenido a la API del Parqueadero"
        })

    # Registrar el Blueprint de las rutas de parqueadero
    app.register_blueprint(parqueadero_bp, url_prefix='/api/v1/parqueadero')

    return app