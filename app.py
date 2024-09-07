from flask import render_template

# models
from src.models.Patient import Patient
from src.models.Appointment import Appointment
from src.models.Business import Business

from src import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)