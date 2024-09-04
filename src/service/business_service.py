from src.extensions import db
from src.models.Business import Business
from flask import jsonify

# C
def create_business_service(name, phone):
     new_business = Business(name, phone)
     db.session.add(new_business)
     db.session.commit()

# R
def retrieve_business_serivce(business_id):
     business = Business.query.get(business_id)
     if business is None:
          return jsonify({'error': 'Business not found'}), 404
     else:
          return jsonify(business.to_dict())
     
# U