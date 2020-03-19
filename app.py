from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

reponses = []

@app.route('/')
def survey_start():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template("survey_start.html", title=title,instructions=instructions)

@app.route('/questions/<question_num>')
def survey_question(question_num)

