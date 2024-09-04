# registration of blueprints
from src.routes.business_route import business_bp

from src.routes.test_route import test_bp

def register_blueprints(app):
     app.register_blueprint(business_bp, url_prefix='/business')
     app.register_blueprint(test_bp, url_prefix='/test')
     