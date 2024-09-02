from app import db

class Appointment(db.Model):
     appointment_id = db.Column(db.Integer, primary_key=True)
     patient_id = db.Column(db.Integer, nullable=False)
     business_id = db.Column(db.Integer, nullable=False)
     time = db.Column(db.Time, nullable=False)
     date = db.Column(db.Date, nullable=False)

     def __init__(self, patient_id, time, date):
          self.patient_id = patient_id
          self.time = time
          self.date = date
          

