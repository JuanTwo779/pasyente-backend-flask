# registration of blueprints
from src.routes.test_route import test_bp
from src.routes.business_route import business_bp
from src.routes.patient_route import patient_bp
from src.routes.appointment_route import appointment_bp

def register_blueprints(app):
     app.register_blueprint(business_bp, url_prefix='/business')
     app.register_blueprint(test_bp, url_prefix='/test')
     app.register_blueprint(patient_bp, url_prefix='/patient')
     app.register_blueprint(appointment_bp, url_prefix='/appointment')
     