from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, DateField
from wtforms.validators import DataRequired

class NamerForm(FlaskForm):
     name = StringField("What's your name?", validators=[DataRequired()])
     submit = SubmitField("Submit")  

class BusinessesForm(FlaskForm):
     query = StringField("Enter business name", validators=[DataRequired()])
     search = SubmitField("Search")

class NewBusinessForm(FlaskForm):
     name = StringField("Enter your business's name here:", validators=[DataRequired()])
     phone = StringField("Enter your business's phone number here:", validators=[DataRequired()])
     create = SubmitField("Create")

class PatientsForm(FlaskForm):
     query = StringField("Search patient by name or phone", validators=[DataRequired()])
     search = SubmitField("Search")

class NewPatientForm(FlaskForm):
     first_name = StringField("Enter patient's given name", validators=[DataRequired()])
     last_name = StringField("Enter patient's surname", validators=[DataRequired()])
     phone = StringField("Enter patient's mobile phone for SMS messaging", validators=[DataRequired()])
     create = SubmitField("Create")

class NewAppointmentForm(FlaskForm):
     time = TimeField("Enter appointment time", validators=[DataRequired()])
     date = DateField("Enter appointment date", validators=[DataRequired()])
     create = SubmitField("Create")