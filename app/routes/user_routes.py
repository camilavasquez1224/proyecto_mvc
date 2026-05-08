from flask import Blueprint, request, jsonify
from app.controllers.user_controller import (
    get_all_users, get_user, create_user, update_user, delete_user
)

user_bp = Blueprint('users', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
def list_users():
    return jsonify(get_all_users())

@user_bp.route('/<int:id>', methods=['GET'])
def show_user(id):
    user = get_user(id)
    return jsonify(user) if user else ('No encontrado', 404)

@user_bp.route('/', methods=['POST'])
def new_user():
    return jsonify(create_user(request.json)), 201

@user_bp.route('/<int:id>', methods=['PUT'])
def edit_user(id):
    user = update_user(id, request.json)
    return jsonify(user) if user else ('No encontrado', 404)

@user_bp.route('/<int:id>', methods=['DELETE'])
def remove_user(id):
    result = delete_user(id)
    return jsonify(result) if result else ('No encontrado', 404)

@user_bp.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200