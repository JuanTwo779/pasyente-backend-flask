from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

# Flask instance
app = Flask(__name__)

# Add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialise database
db = SQLAlchemy(app)

# create model
class Business(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(200), nullable=False, unique=True)
     phone = db.Column(db.String(12), nullable=False, unique=True)
     date_added = db.Column(db.DateTime, default=datetime.now(timezone.utc))

     def __init__(self, name, phone):
          self.name = name
          self.phone = phone

     # Create A String
     def __repr__(self):
          return f'<>'

# Create route decorator
@app.route("/")
def index():
     return "<h1>Hello mate</h1>"
     # return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)