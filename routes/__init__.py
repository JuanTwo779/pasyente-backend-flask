# blueprints
from routes.business_route import business_bp
def register_blueprints(app):
     app.register_blueprint(business_bp, url_prefix='/business')
     