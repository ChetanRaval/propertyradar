from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for your data
class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(120), unique=True, nullable=False)
    beds = db.Column(db.Integer, nullable=True)
    baths = db.Column(db.Integer, nullable=True)
    cars = db.Column(db.Integer, nullable=True)
    price = db.Column(db.Float, nullable=True)
    price_per_sqm = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f'Listing("{self.url}", Beds: {self.beds}, Baths: {self.baths}, Cars: {self.cars}, Price: {self.price}, Price/SqM: {self.price_per_sqm})'

@app.route('/')
def index():
    return 'Hello, Flask with Database!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
