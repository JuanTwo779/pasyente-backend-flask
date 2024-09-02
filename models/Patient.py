from app import db
from datetime import datetime, timezone

class Patient(db.Model):
     patient_id = db.Column(db.Integer, primary_key=True)
     business_id = db.Column(db.Integer, db.ForeignKey('business.business_id'), nullable=False)
     first_name = db.Column(db.String(200), nullable=False, unique=True)
     last_name = db.Column(db.String(200), nullable=False, unique=True)
     phone = db.Column(db.String(15), nullable=False, unique=True)
     date_added = db.Column(db.DateTime, default=datetime.now(timezone.utc))

     # relationships
     business = db.relationship('Business', backref='patients', lazy=True)
     appointments = db.relationship('Appointment', backref='patient', lazy=True)

     def __init__(self, business_id, first_name, last_name, phone, date_added):
          self.business_id = business_id
          self.first_name = first_name
          self.last_name = last_name
          self.phone = phone
          self.date_added = date_added