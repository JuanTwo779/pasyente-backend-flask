
# models
from src.models.Patient import Patient
from src.models.Appointment import Appointment
from src.models.Business import Business

from src import create_app

app = create_app()

# Create route decorator
@app.route("/")
def index():
     return "<h1>Hello mate</h1>"
     # return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)