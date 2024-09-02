from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime, timezone

# Flask instance
app = Flask(__name__)

# Add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://JuanMangubat:Hansosjsneia-09@localhost:3307/pasyente_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialise database
db = SQLAlchemy(app)

# migration
migrate = Migrate(app, db)

# create model
from models.Patient import Patient
from models.Appointment import Appointment
from models.Business import Business


# Create route decorator
@app.route("/")
def index():
     return "<h1>Hello mate</h1>"
     # return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)