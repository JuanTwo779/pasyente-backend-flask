from src.extensions import db
from src.models.Appointment import Appointment
from src.models.Business import Business
from src.models.Patient import Patient
from datetime import datetime

# C
def create_appointment_service(patient_id, business_id, time, date):
     # check business exists
     # business = Business.query.get(business_id)
     # if not business:
     #      raise ValueError('Invalid business_id: Business does not exist')
     
     # check patient exists
     patient = Patient.query.get(patient_id)
     if not patient:
          raise ValueError('Invalid patient_id: Patient does not exist')
     
     # create appointment 
     appointment_time = datetime.strptime(time, '%H:%M:%S').time()
     appointment_date = datetime.strptime(date, '%d-%m-%Y').date()
     new_appointment = Appointment(
          patient_id=patient_id, 
          business_id=business_id, 
          time=appointment_time, 
          date=appointment_date)

     try:
          db.session.add(new_appointment)
          db.session.commit()
          return new_appointment
     except Exception as e:
          db.session.rollback()
          raise e
     
# R
def retrieve_appointment_service(appointment_id):
     appointment = Appointment.query.get(appointment_id)
     if appointment is None:
          raise ValueError('Invalid appointment_id: Appointment does not exist')
     else:
          return appointment
     
# U
def update_appointment_service(appointment_id, time, date):
     appointment = Appointment.query.get(appointment_id)
     if appointment is None:
          raise ValueError('Invalid appointment_id: Appointment does not exist')
     else:
          appointment_time = datetime.strptime(time, '%H:%M:%S').time()
          appointment_date = datetime.strptime(date, '%d-%m-%Y').date()
          appointment.time = appointment_time
          appointment.date = appointment_date
          db.session.commit()
          return appointment
     
# D
def delete_appoint_service(appointment_id):
     appointment = Appointment.query.get(appointment_id)
     if appointment is None:
          raise ValueError('Invalid appointment_id: Appointment does not exist')
     else:
          db.session.delete(appointment)
          db.session.commit()