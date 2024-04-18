# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from random import shuffle

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mcq_database.db'
db = SQLAlchemy(app)

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

# Define the Question model
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(500), nullable=False)
    option_a = db.Column(db.String(100), nullable=False)
    option_b = db.Column(db.String(100), nullable=False)
    option_c = db.Column(db.String(100), nullable=False)
    option_d = db.Column(db.String(100), nullable=False)
    correct_answer = db.Column(db.String(1), nullable=False)
    level = db.Column(db.Integer, nullable=False)

# Define routes for candidate form and submission
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

# Define route for displaying multiple choice questions
@app.route('/mcq', methods=['GET', 'POST'])
def mcq():
    if request.method == 'POST':
        # Process MCQ form submission
        score = 0
        for question_id in request.form:
            question = Question.query.get(question_id)
            if question and request.form[question_id] == question.correct_answer:
                score += 1
        return redirect(url_for('results', score=score))

    # Fetch all questions from the database
    questions = Question.query.all()
    # Shuffle the questions to provide a different order each time
    shuffle(questions)
    return render_template('mcq.html', questions=questions)
@app.route('/submit_mcq', methods=['POST'])
def submit_mcq():
    score = 0
    # Iterate through each question and check the user's answer
    for question in Question.query.all():
        user_answer = request.form.get(f"question{question.id}")
        if user_answer == question.correct_answer:
            score += 1
    
    # Redirect to the results page with the score as a parameter
    return redirect(url_for('results', score=score))
# Define route for displaying the results
@app.route('/results')
def results():
    score = request.args.get('score')
    return render_template('results.html', score=score)

if __name__ == "__main__":
    # Create the database tables inside the Flask application context
    with app.app_context():
        db.create_all()
    app.run(debug=True)
