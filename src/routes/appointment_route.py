from flask import Blueprint, request, jsonify

appointment_bp = Blueprint('appointment', __name__)

# create
from src.service.appointment_service import create_appointment_service
@appointment_bp.route('/create', methods=['POST'])
def create_appointment():
     data = request.get_json()
     if not data or 'patient_id' not in data or 'business_id' not in data or 'time' not in data or 'date' not in data:
          return jsonify({'error': 'Missing required parameters'}), 400
     
     try:
          new_appointment = create_appointment_service(
               data['patient_id'], data['business_id'],
               data['time'], data['date']
          )
          return jsonify(new_appointment.to_dict()), 201
     except ValueError as ve:
         return jsonify({'error': str(ve)}), 404
     except Exception as e:
         return jsonify({'error': str(e)}), 400
     
# read, update, delete
from src.service.appointment_service import retrieve_appointment_service, update_appointment_service, delete_appoint_service
@appointment_bp.route('/<int:appointment_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_appointment(appointment_id):
     if request.method == 'GET':
          try:
               appointment = retrieve_appointment_service(appointment_id)
               return jsonify(appointment.to_dict()), 200
          except Exception as e:
               return {'error': str(e)}, 500
          
     elif request.method == 'PUT':
          data = request.get_json()
          if not data or 'time' not in data or 'date' not in data:
               return jsonify({'error':'Missing required paramters'}), 400
          

          try:
               appointment = update_appointment_service(appointment_id, data['time'], data['date'])
               return jsonify(appointment.to_dict())
          except ValueError as ve:
              return jsonify({'error': str(ve)}), 404
          except Exception as e:
              return jsonify({'status': 'error', 'message': str(e)}), 500
          
     elif request.method == 'DELETE':
          try:
               delete_appoint_service(appointment_id)
               return ('Appointment with Id "{}" deleted successfully').format(appointment_id)
          except ValueError as ve:
               return jsonify({'error': str(ve)}), 404
          except Exception as e:
               return jsonify({'status': 'error', 'message': str(e)}), 500