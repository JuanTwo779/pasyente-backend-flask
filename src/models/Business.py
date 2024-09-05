from src.extensions import db
from datetime import datetime, timezone


class Business(db.Model):
     business_id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(200), nullable=False, unique=True)
     phone = db.Column(db.String(15), nullable=False, unique=True)
     date_added = db.Column(db.DateTime, default=datetime.now(timezone.utc))

     # Reverse relationship to patient
     patient = db.relationship('Patient', backref='business')

     def __init__(self, name, phone):
          self.name = name
          self.phone = phone

     def to_dict(self):
          return {
               'id': self.business_id,
               'name': self.name,
               'phone': self.phone,
               'date_added': self.date_added
          }

# from src.models.Patient import Patient
# from src.models.Appointment import Appointment

# Business.patients = db.relationship('Patient', backref='business', lazy=True)
# Business.appointment = db.relationship('Appointment', backref='business', lazy=True)