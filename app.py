# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mcq_database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Candidate model
class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone_number = db.Column(db.String(10), nullable=False)
    alt_phone_number = db.Column(db.String(10))
    semester = db.Column(db.Integer, nullable=False)
    stream = db.Column(db.String(100), nullable=False)
    college_name = db.Column(db.String(100), nullable=False)
    placement_officer_name = db.Column(db.String(100))
    placement_officer_email = db.Column(db.String(100))
    placement_officer_phone = db.Column(db.String(10))
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)

# Define routes
@app.route('/')
def candidate_form():
    return render_template('candidate_form.html')

@app.route('/submit', methods=['POST'])
def submit_candidate():
    # Process candidate form submission
    name = request.form['name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    alt_phone_number = request.form.get('alt_phone_number', '')
    semester = request.form['semester']
    stream = request.form['stream']
    college_name = request.form['college_name']
    placement_officer_name = request.form.get('placement_officer_name', '')
    placement_officer_email = request.form.get('placement_officer_email', '')
    placement_officer_phone = request.form.get('placement_officer_phone', '')
    city = request.form['city']
    state = request.form['state']
    
    # Create a new candidate instance and add it to the database
    new_candidate = Candidate(
        name=name, email=email, phone_number=phone_number, 
        alt_phone_number=alt_phone_number, semester=semester, 
        stream=stream, college_name=college_name, 
        placement_officer_name=placement_officer_name, 
        placement_officer_email=placement_officer_email, 
        placement_officer_phone=placement_officer_phone, 
        city=city, state=state
    )
    db.session.add(new_candidate)
    db.session.commit()
    return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

# Move db.create_all() inside the if __name__ == "__main__" block
if __name__ == "__main__":
    # Create the database tables inside the Flask application context
    with app.app_context():
        db.create_all()
    app.run(debug=True)
