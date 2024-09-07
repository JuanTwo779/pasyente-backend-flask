from flask import Blueprint, request, jsonify, flash, redirect, url_for, render_template
from src.models.Business import Business
from src.extensions import db

business_bp = Blueprint('business', __name__)

from src.service.business_service import retrieve_businesses_serivce_by_name
@business_bp.route('/search-business', methods=['GET', 'POST'])
def search_business():
     if request.method == 'POST':
          # # Get search query
          search_query = request.form.get('search_query')
          # # Get businesses given the query
          businesses = retrieve_businesses_serivce_by_name(search_query)
          # # Create new business if no results
          if not businesses:
               flash('No businesses found, Please create a new business.')
               return redirect(url_for('new_business'))
          # # Go to selection page if there are results
          return render_template('select_business.html', businesses=businesses)
     
     # Main serach business template
     return render_template('search_business.html')

# get all
from src.service.business_service import list_all_business_service
@business_bp.route('/list', methods=['GET'])
def list_all_business():
     try:
          return jsonify(list_all_business_service())
     except Exception as e:
          return {'error': str(e)}, 500

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


# read, update, delete
from src.service.business_service import retrieve_business_serivce
from src.service.business_service import update_business_service
from src.service.business_service import delete_business_service
@business_bp.route('/<int:business_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_business(business_id):
     if request.method == 'GET':
          try:
               business = retrieve_business_serivce(business_id)
               return jsonify(business.to_dict()), 200
          except Exception as e:
               return {'error': str(e)}, 500
          
     elif request.method == 'PUT':
          data = request.get_json()

          if not data or 'name' not in data or 'phone' not in data:
               return jsonify({'error': 'Missing required parameters'}), 400
          
          try:
               updated_business = update_business_service(business_id, data['name'], data['phone'])
               return jsonify(updated_business.to_dict()), 200
          except ValueError as ve:
               return jsonify({'error': str(ve)}), 404
          except Exception as e:
               return jsonify({'status': 'error', 'message': str(e)}), 500
          
     elif request.method == 'DELETE':
          try:
               return delete_business_service(business_id)
          except Exception as e:
               return {'error': str(e)}, 500