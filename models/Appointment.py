from app import db

class Appointment(db.Model):
     appointment_id = db.Column(db.Integer, primary_key=True)
     patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'), nullable=False)
     business_id = db.Column(db.Integer, db.ForeignKey('business.business_id'), nullable=False)
     time = db.Column(db.Time, nullable=False)
     date = db.Column(db.Date, nullable=False)

     patient = db.relationship('Patient', backref='appointments', lazy=True)
     business = db.relationship('Business', backref='appointments', lazy=True)

     def __init__(self, patient_id, business_id, time, date):
          self.patient_id = patient_id
          self.business_id = business_id
          self.time = time
          self.date = date