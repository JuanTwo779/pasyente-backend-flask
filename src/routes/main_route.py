from flask import Blueprint, render_template, flash, redirect, request, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, DateField
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

     business_id = request.args.get('business_id')

     if form.validate_on_submit():
          search_query = form.query.data
          patients = retrieve_patient_serivce_by_name_or_phone(search_query)
          if not patients:
               flash("Create a new patient")

     return render_template("search_patient.html",
          patients = patients,
          form = form,
          business_id = business_id)

# 2.1) SELECT PATIENT
@main_bp.route('/select-patient', methods=["POST"])
def select_patient():
     selected_business_id = request.args.get('business_id')
     selected_patient_id = request.form.get('selected_patient')

     if not selected_patient_id:
          flash('Please select a patient to continue.', 'warning')
          return render_template('search_patient.html', patients=[], form = PatientsForm(), business_id=selected_business_id)
     
     return redirect(url_for('main.create_new_appointment', business_id=selected_business_id, patient_id=selected_patient_id))

# 2.2) CREATE NEW PATIENT
class NewPatientForm(FlaskForm):
     first_name = StringField("Enter patient's given name", validators=[DataRequired()])
     last_name = StringField("Enter patient's surname", validators=[DataRequired()])
     phone = StringField("Enter patient's mobile phone for SMS messaging", validators=[DataRequired()])
     create = SubmitField("Create")

from src.service.patient_service import create_patient_service
@main_bp.route("/create-patient", methods=["GET", "POST"])
def create_new_patient():
     form = NewPatientForm()
     business_id = request.args.get('business_id')

     if form.validate_on_submit():
          first_name = form.first_name.data
          last_name = form.last_name.data
          phone = form.phone.data
          create_patient_service(business_id=business_id,
                                 first_name=first_name,
                                 last_name=last_name,
                                 phone=phone)
          flash("Patient successfully created")
          return render_template("search_patient.html", patients = [], form = PatientsForm(), business_id = business_id)

     return render_template('create_patient.html', form = form, business_id=business_id)

# 3) CREATE APPOINTMENT FOR PATIENT - needs work
class NewAppointmentForm(FlaskForm):
     time = TimeField("Enter appointment time", validators=[DataRequired()])
     date = DateField("Enter appointment date", validators=[DataRequired()])
     create = SubmitField("Create")

from src.service.business_service import retrieve_business_serivce
from src.service.patient_service import retrieve_patient_service
from src.service.appointment_service import create_appointment_service
@main_bp.route("/create_appointment", methods=["GET", "POST"])
def create_new_appointment():

     if 'appointments' not in session:
        session['appointments'] = []

     form = NewAppointmentForm()
     # reintroduce queries in html when posting
     business_id = request.args.get('business_id', type=int)
     patient_id = request.args.get('patient_id', type=int)

     business = retrieve_business_serivce(business_id=business_id)
     patient = retrieve_patient_service(patient_id=patient_id)

     if form.validate_on_submit():
          time = form.time.data
          date = form.date.data
          formatted_time = time.strftime("%I:%M %p")  # 12-hour time with AM/PM
          formatted_date = date.strftime("%B %d, %Y")

          # add appointment to session list
          session['appointments'].append({
               "patient_id": patient_id,
               "business_id": business_id,
               "time": formatted_time,
               "date": formatted_date
          })
          session.modified = True

          flash("Appointment created")
          return redirect(url_for("main.draft_appointments", business_id=business_id, patient_id=patient_id))

     return render_template('create_appointment.html', form=form, 
                            business=business, 
                            patient=patient)


# send SMS + save appointment list to DB, clear session list
from src.models.Patient import Patient
@main_bp.route("/draft-appointments", methods=['GET'])
def draft_appointments():
     appointments = session.get('appointments', [])
     patient_ids = {appointment['patient_id'] for appointment in appointments}

     # Query all patients associated with the appointments -> move to service
     patients = Patient.query.filter(Patient.patient_id.in_(patient_ids)).all()
     patient_map = {patient.patient_id: patient for patient in patients}

     return render_template("draft_appointments.html", appointments=appointments, patient_map=patient_map)