from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import text, inspect
from dotenv import load_dotenv
import os


# load environment variables
load_dotenv()

# Flask instance
app = Flask(__name__)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Blueprints
from routes import register_blueprints
register_blueprints(app)


# secret env test
# @app.route("/test_env")
def test_env():
     env = os.getenv("DATABASE_URL")
     if env is None:
          return jsonify({'status': 'error', 'result': env})
     else:
          return jsonify({'status': 'success', 'result': env})


# db test
# @app.route("/test_db")
def test_db():
     try:
          # result = db.session.execute(text('SELECT 1'))
          inspector = inspect(db.engine)
          result = inspector.get_table_names()
          return jsonify({'status': 'success', 'result': result})
     except Exception as e:
          return jsonify({'status': 'error', 'message': str(e)})


# models
# from models.Patient import Patient
# from models.Appointment import Appointment
# from models.Business import Business


# Create route decorator
@app.route("/")
def index():
     return "<h1>Hello mate</h1>"
     # return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)