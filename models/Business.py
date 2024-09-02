from app import db, datetime, timezone

class Business(db.Model):
     business_id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(200), nullable=False, unique=True)
     phone = db.Column(db.String(12), nullable=False, unique=True)
     date_added = db.Column(db.DateTime, default=datetime.now(timezone.utc))

     def __init__(self, name, phone, date_added):
          self.name = name
          self.phone = phone
          self.date_added = date_added