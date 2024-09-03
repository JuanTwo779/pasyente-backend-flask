from flask import Blueprint, request, jsonify
from models.Business import Business


business_bp = Blueprint('business', __name__)


# create
@business_bp.route('/create')
def create_business():
     from app import db

     data = request.get_json()
     
     business_name = data.get('name')
     business_num = data.get('phone')

     if not business_name or not business_num:
          return jsonify({'error': 'Missing required parameters'}), 400
     
     new_business = Business(business_name, business_num)

     # add business to DB
     db.session.add(new_business)
     db.session.commit()
     
     return jsonify({'status': 'success', 'business': {'name': business_name, 'phone': business_num}}), 201

# remove (not accessible)

# update

# edit