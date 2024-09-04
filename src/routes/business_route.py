from flask import Blueprint, request, jsonify
from src.models.Business import Business
from src.extensions import db

business_bp = Blueprint('business', __name__)


# create
from src.service.business_service import create_business_service
@business_bp.route('/create', methods=['POST'])
def create_business():
     data = request.get_json() 
     
     # validations
     if not data or 'name' not in data or 'phone' not in data:
          return jsonify({'error': 'Missing required parameters'}), 400
     
     try:
          create_business_service(data['name'], data['phone'])
          return jsonify({'message': 'Business created successfully'}), 201
     except Exception as e:
          db.session.rollback()
          return jsonify({'status': 'error', 'message': str(e)}), 409

# read
from src.service.business_service import retrieve_business_serivce
@business_bp.route('/<business_id>', methods=['GET'])
def retrieve_business(business_id):
     try:
          return retrieve_business_serivce(business_id)
     except Exception as e:
          return {'error': str(e)}, 500

# update
from src.service.business_service import update_business_service
@business_bp.route('/<business_id>', methods=['PUT'])
def update_business(business_id):
     data = request.get_json()

     if not data or 'name' not in data or 'phone' not in data:
          return jsonify({'error': 'Missing required parameters'}), 400
     
     try:
          updated_business = update_business_service(business_id, data['name'], data['phone'])
          return jsonify(updated_business.to_dict()), 200
     except ValueError as ve:
        # Handle specific errors, like 'Business not found'
        return jsonify({'error': str(ve)}), 404
     except Exception as e:
        # Handle other exceptions
        return jsonify({'status': 'error', 'message': str(e)}), 500

# delete (not accessible)
from src.service.business_service import delete_business_service
@business_bp.route('/<business_id>', methods=['DELETE'])
def delete_business(business_id):
     try:
          return delete_business_service(business_id)
     except Exception as e:
          return {'error': str(e)}, 500

# get all
from src.service.business_service import list_all_business_service
@business_bp.route('/', methods=['GET'])
def list_all_business():
     try:
          return jsonify(list_all_business_service())
     except Exception as e:
          return {'error': str(e)}, 500