# Endpoints HTTP (API REST)
from flask import Blueprint, request, jsonify
from app.services.parqueadero_service import parqueadero_service

parqueadero_bp = Blueprint('parqueadero', __name__)

@parqueadero_bp.route('/ingreso', methods=['POST'])
def ingresar():
    data = request.get_json() or {}
    placa = data.get('placa')
    if not placa:
        return jsonify({"error": "La placa es obligatoria"}), 400

    try:
        registro = parqueadero_service.ingresar_moto(placa)
        return jsonify({"mensaje": "Moto ingresada correctamente", "data": registro}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 409

@parqueadero_bp.route('/salida', methods=['POST'])
def salir():
    data = request.get_json() or {}
    placa = data.get('placa')
    if not placa:
        return jsonify({"error": "La placa es obligatoria"}), 400

    try:
        factura = parqueadero_service.procesar_salida(placa)
        return jsonify({"mensaje": "Salida procesada", "factura": factura}), 200
    except KeyError as e:
        return jsonify({"error": str(e)}), 404

@parqueadero_bp.route('/motos', methods=['GET'])
def listar():
    motos = parqueadero_service.listar_motos()
    return jsonify({"motos_activas": motos, "total": len(motos)}), 200