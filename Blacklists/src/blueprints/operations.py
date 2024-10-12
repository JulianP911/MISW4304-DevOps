from flask import jsonify, request, Blueprint, Response
from models.model import Blacklist, BlacklistJsonSchema, db

operations_blueprint = Blueprint('operations', __name__)

@operations_blueprint.route('/blacklists', methods=['POST'])
def blacklist():
    data = request.json
    email = data.get('email')
    app_uuid = data.get('app_uuid')
    blocked_reason = data.get('blocked_reason')

    if not email or not app_uuid or not blocked_reason:
        Response(status=400)

    try:
        new_post = Blacklist(email=email, app_uuid=app_uuid, blocked_reason=blocked_reason)
        db.session.add(new_post)
        db.session.commit()
        return BlacklistJsonSchema().dump(new_post), 200
    except KeyError:
        return jsonify({"error": "Error al agregar email a lista negra"}), 400

@operations_blueprint.route('/blacklists/ping', methods=['GET'])
def health_check():
    return Response('pong', status=200)
