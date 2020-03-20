from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)



responses = []
quest_number = 0

@app.route('/')
def survey_start():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template("survey_start.html", title=title,
    instructions=instructions)

@app.route('/questions/<question_num>')
def survey_question(question_num):
    question_number = int(question_num)

    if not question_number == quest_number:
        url = f'/questions/{quest_number}'
        return redirect(url)

    question_obj = satisfaction_survey.questions[question_number]
    question = question_obj.question
    choices = question_obj.choices

    # breakpoint()

    return render_template("survey_question.html", question=question, choices=choices)

@app.route('/answer', methods=["POST"])
def process_answers():
    """
    store answers from post request in responses list and 
    redirect user to next question or thank you page if
    no more questions
    """

    global responses
    global quest_number

    question = satisfaction_survey.questions[quest_number].question
    responses.append(request.form[question])
    # breakpoint()

    quest_number = quest_number + 1
    

    if quest_number < len(satisfaction_survey.questions):
        url=f'/questions/{quest_number}'
    else:
        url = '/thanks'

    return redirect(url)

@app.route('/thanks')
def survey_end():
    """
    Creates the thank you page at the end of the survey
    """
    return render_template("thanks.html")
