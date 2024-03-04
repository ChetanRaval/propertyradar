from urllib.parse import urlparse
from flask import Flask, request, redirect, url_for, render_template
from scrapers.scraper import scrape_listing 

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

# Function to validate the URL input in the form submission
def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

# # Route to display the form
# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        submitted_url = request.form['url']
        # Use the scrape_listing function from scraper.py
        listing_data = scrape_listing(submitted_url)
        
        # Further processing, like saving data to the database
        
        return redirect(url_for('index'))

    return render_template('index.html')


# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        submitted_url = request.form['url']

        # Validate the URL
        if is_valid_url(submitted_url):
            # If the URL is valid, you can proceed with your logic to handle the URL
            # such as scraping and storing data
            print(f"Valid URL submitted: {submitted_url}")

            # Redirect back to the homepage after successful submission
            return redirect(url_for('index'))
        else:
            # If the URL is not valid, you might want to inform the user
            # For now, let's just print a message to the console
            print("Invalid URL submitted")

            # Redirect back to the homepage or show an error message
            return redirect(url_for('index'))  # Consider adding a query parameter or flash message to indicate the error


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)