from flask import Blueprint, request, jsonify
from src.extensions import db

patient_bp = Blueprint('patient', __name__)

# list all w/ business id

# list all w/ patient id

# list all

# create
from src.service.patient_service import create_patient_service
@patient_bp.route('/create', methods=['POST'])
def create_patient():
     data = request.get_json()
     if not data or 'business_id' not in data or 'first_name' not in data or 'last_name' not in data or 'phone' not in data:
        return jsonify({'error': 'Missing required parameters'}), 400

     try:
          new_patient = create_patient_service(
              data['business_id'], data['first_name'], 
              data['last_name'], data['phone'])
          return jsonify(new_patient.to_dict()), 201
     except ValueError as ve:
         return jsonify({'error': str(ve)}), 404
     except Exception as e:
         return jsonify({'error': str(e)}), 400
         
# read, update, delete
from src.service.patient_service import retrieve_patient_service
from src.service.patient_service import update_patient_service
from src.service.patient_service import delete_patient_service
@patient_bp.route('/<int:patient_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_patient(patient_id):
     if request.method == 'GET':
        try:
            patient = retrieve_patient_service(patient_id)
            return jsonify(patient.to_dict()), 200
        except Exception as e:
            return {'error': str(e)}, 500
     
     elif request.method == 'PUT':
          data = request.get_json()
          if not data or 'first_name' not in data or 'last_name' not in data or 'phone' not in data:
              return jsonify({'error': 'Missing required parameters'}), 400 

          try:
              patient = update_patient_service(patient_id, data['first_name'], data['last_name'], data['phone'])
              return jsonify(patient.to_dict()), 200
          except ValueError as ve:
              return jsonify({'error': str(ve)}), 404
          except Exception as e:
              return jsonify({'status': 'error', 'message': str(e)}), 500
          
     elif request.method == 'DELETE':
         try:
             delete_patient_service(patient_id)
             return ('Patient with Id "{}" deleted successfully').format(patient_id)
         except ValueError as ve:
             return jsonify({'error': str(ve)}), 404
         except Exception as e:
             return jsonify({'status': 'error', 'message': str(e)}), 500