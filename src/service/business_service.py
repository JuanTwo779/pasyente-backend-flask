from src.extensions import db
from src.models.Business import Business
from flask import jsonify

# Get by name
def retrieve_businesses_serivce_by_name(search_query):
     businesses = Business.query.filter(Business.name.contains(search_query))
     return businesses

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
          return business
     
# U
def update_business_service(business_id, name, phone):
     business = Business.query.get(business_id)
     if business is None:
          return jsonify({'error': 'Business not found'}), 404
     else:
          business.name = name
          business.phone = phone
          db.session.commit()
          return business

# D
def delete_business_service(business_id):
     business = Business.query.get(business_id)
     if business is None:
          return jsonify({'error': 'Business not found'}), 404
     else:
          db.session.delete(business)
          db.session.commit()
          return ('Business account with Id "{}" deleted successfully').format(business_id)
          
# R all
def list_all_business_service():
     businesses = Business.query.all()
     response = []
     for business in businesses: response.append(business.to_dict())
     return response