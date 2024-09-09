from flask import Blueprint, render_template, flash, redirect, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def index():
     return render_template("index.html")


# test form
class NamerForm(FlaskForm):
     name = StringField("What's your name?", validators=[DataRequired()])
     submit = SubmitField("Submit")     

@main_bp.route("/name", methods=['GET', "POST"])
def name():
     name = None
     form = NamerForm()
     # Validate
     if form.validate_on_submit():
          name = form.name.data
          form.name.data = ''
          flash('Form submitted successfully')
          
     return render_template("name.html",
          name = name,
          form = form)

# 1) SEARCH FOR BUSINESS
class BusinessesForm(FlaskForm):
     query = StringField("Enter business name", validators=[DataRequired()])
     search = SubmitField("Search")

from src.service.business_service import retrieve_businesses_serivce_by_name
@main_bp.route("/search-business", methods=["GET", "POST"])
def search_business_name():
     form = BusinessesForm()
     businesses = []

     if form.validate_on_submit():
          search_query = form.query.data
          businesses = retrieve_businesses_serivce_by_name(search_query)
          if not businesses:
               flash("Business does not exist. Please contact us at 0481988967")

     return render_template("search_business.html",
          businesses = businesses,
          form = form)

# 1.1) SELECT BUSINSESS
@main_bp.route("/select-business", methods=["POST"])
def select_business():
     selected_business_id = request.form.get('selected_business') #pass on to next page

     if not selected_business_id:
          flash('Please select a business to continue.', 'warning')
          return redirect(url_for('main.search_business_name'))
     
     return redirect(url_for('main.search_patient', business_id=selected_business_id))

# 1.2) CREATE NEW BUSINESS
class NewBusinessForm(FlaskForm):
     name = StringField("Enter your business's name here:", validators=[DataRequired()])
     phone = StringField("Enter your business's phone number here:", validators=[DataRequired()])
     create = SubmitField("Create")

from src.service.business_service import create_business_service
@main_bp.route("/create-business", methods=["GET", "POST"])
def create_new_business():
     form = NewBusinessForm()

     if form.validate_on_submit():
          name = form.name.data
          phone = form.phone.data
          create_business_service(name=name, phone=phone)
          flash("Business: " + name + " successfully created!")
          return render_template('search_business.html', form = BusinessesForm())
     
     return render_template('create_business.html', form = form)

# 2) SEARCH FOR PATIENTS
class PatientsForm(FlaskForm):
     query = StringField("Search patient by name or phone", validators=[DataRequired()])
     search = SubmitField("Search")

from src.service.patient_service import retrieve_patient_serivce_by_name_or_phone
@main_bp.route("/search-patient", methods=["GET", "POST"])
def search_patient():
     form = PatientsForm()
     patients = []

     business_id = request.form.get('business_id')

     if form.validate_on_submit():
          search_query = form.query.data
          patients = retrieve_patient_serivce_by_name_or_phone(search_query)
          if not patients:
               flash("Create a new patient")

     return render_template("search_patient.html",
          patients = patients,
          form = form)

# 2.1) SELECT PATIENT
@main_bp.route('/select-patient', methods=["POST"])
def select_patient():
     selected_business_id = request.form.get('business_id')
     selected_patient_id = request.form.get('selected_patient')

     # if not selected_business_id:
     #      flash('Please select a patient to continue.', 'warning')
     #      return redirect(url_for('main.search_patient'))
     
     return redirect(url_for('main.make_appointment', business_id=selected_business_id, patient_id=selected_patient_id))


