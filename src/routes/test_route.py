from flask import Blueprint, request, jsonify
from sqlalchemy import inspect, text
from src.extensions import db

test_bp = Blueprint('test', __name__)

@test_bp.route("/database")
def test_db():
     try:
          # inspector = inspect(db.engine)
          # result = inspector.get_table_names()
          # return jsonify({'status': 'success', 'result': result})
          # result = db.session.execute(text('SELECT 1'))
          result = db.session.execute(text('SELECT 1')).fetchone()
          return jsonify({'status': 'success', 'result': result[0]})
     except Exception as e:
          return jsonify({'status': 'error', 'message': str(e)})
     
@test_bp.route("/secret")
def test_secret():
     import os
     env = os.getenv("DATABASE_URL")
     if env is None:
          return jsonify({'status': 'error', 'result': env})
     else:
          return jsonify({'status': 'success', 'result': env})

