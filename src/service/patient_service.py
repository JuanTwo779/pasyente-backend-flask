from src.extensions import db
from src.models.Patient import Patient
from src.models.Business import Business

# Retrieve by name or phone
def retrieve_patient_serivce_by_name_or_phone(search_query):
     patients = Patient.query.filter((Patient.first_name.contains(search_query)) | 
                                    (Patient.phone.contains(search_query)) |
                                    (Patient.last_name.contains(search_query))).all()
     return patients

# C
def create_patient_service(business_id, first_name, last_name, phone):
     # check business exists
     business = Business.query.get(business_id)
     if not business:
          raise ValueError('Invalid business_id: Business does not exist')
     
     # create new patient
     new_patient = Patient(business_id=business_id, first_name=first_name, last_name=last_name, phone=phone)

     try:
          db.session.add(new_patient)
          db.session.commit()
          return new_patient
     except Exception as e:
          db.session.rollback()
          raise e
     
# R
def retrieve_patient_service(patient_id):
     patient = Patient.query.get(patient_id)
     if patient is None:
          raise ValueError('Invalid patient_id: Patient does not exist')
     else:
          return patient
     
# U
def update_patient_service(patient_id, first_name, last_name, phone):
     patient = Patient.query.get(patient_id)
     if patient is None:
          raise ValueError('Invalid patient_id: Patient does not exist')
     else:
          patient.first_name = first_name
          patient.last_name = last_name
          patient.phone = phone
          db.session.commit()
          return patient
     
def delete_patient_service(patient_id):
     patient = Patient.query.get(patient_id)
     if patient is None:
          raise ValueError('Invalid patient_id: Patient does not exist')
     else:
          db.session.delete(patient)
          db.session.commit()