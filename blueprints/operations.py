from flask import jsonify, request, Blueprint, Response
from models.model import Blacklist, BlacklistJsonSchema, db
from dotenv import load_dotenv
import os
import re
from uuid import UUID

load_dotenv()

operations_blueprint = Blueprint('operations', __name__)

# Token predefinido
AUTH_TOKEN = os.environ['TOKEN']

# Función para verificar el token de autorización
def verify_token():
    token = request.headers.get('Authorization')
    if token is not None:
        token = token.split(" ")[-1]
        if token == AUTH_TOKEN:
            return True
    return False

# Función para validar si una cadena es un UUID válido
def is_valid_uuid(uuid_str):
    try:
        UUID(uuid_str, version=4)
        return True
    except ValueError:
        return False

# Permite agregar un email a la lista negra global de la organización
@operations_blueprint.route('/blacklists', methods=['POST'])
def blacklist():
    if not verify_token():
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    email = data.get('email')
    app_uuid = data.get('app_uuid')
    blocked_reason = data.get('blocked_reason')

    request_ip = request.remote_addr
    # Validaciones
    if not email or not app_uuid:
        return jsonify({"error": "Email y app_uuid son obligatorios"}), 400

    if not is_valid_uuid(app_uuid):
        return jsonify({"error": "app_uuid no es un uuid válido"}), 400

    if blocked_reason and len(blocked_reason) > 255:
        return jsonify({"error": "blocked_reason debe tener máximo 255 caracteres"}), 400

    try:
        new_post = Blacklist(email=email, app_uuid=app_uuid, blocked_reason=blocked_reason,request_ip=request_ip)
        db.session.add(new_post)
        db.session.commit()
        return {"msg":"Email agregado a la blacklist", "blacklist":BlacklistJsonSchema().dump(new_post)}, 200
    except Exception as error:
        return jsonify({"error": "Error agregando email a blacklist", "details": str(error)}), 400

# Permite saber si un email está en la lista negra global de la organización o no, y el motivo por el que fue agregado a la lista negra
@operations_blueprint.route('/blacklists/<string:email>', methods=['GET'])
def blacklist_by_id(email):
    if not verify_token():
        return jsonify({"error": "Unauthorized"}), 401

    blacklist =  db.session.query(Blacklist).filter_by(email=email).first()
    if not blacklist:
        return jsonify({"is_blacklisted": False}), 200

    return jsonify({"is_blacklisted": True, "blocked_reason": blacklist.blocked_reason}), 200

@operations_blueprint.route('/blacklists/ping', methods=['GET'])
def health_check():
    return Response('pong', status=200)
