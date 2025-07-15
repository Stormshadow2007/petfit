from flask import Blueprint, jsonify, request
from .pet import pet_status, update_pet

main = Blueprint('main', __name__)

@main.route('/get_pet', methods=['GET'])
def get_pet():
    return jsonify(pet_status)

@main.route('/train_pet', methods=['POST'])
def train_pet():
    data = request.get_json()
    action = data.get('action')
    update_pet(action)
    return jsonify(pet_status)