from flask import Flask, request, render_template, redirect, flash, session
from surveys import satisfaction_survey as survey
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# the toolbar is only enabled in debug mode:
app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'Flexxx123'

toolbar = DebugToolbarExtension(app)

RESPONSES_KEY = "responses"

app.config["SECRET_KEY"] = "labomba"
@app.route("/" )
def hello():
    title = survey.title
    return render_template("survey.html", title=title)

@app.route("/begin", methods=["POST"])
def start():
    session[RESPONSES_KEY] = []
    return redirect("/questions/0")

@app.route("/questions/<int:question_id>")
def questions(question_id):
    
    responses = session.get(RESPONSES_KEY)
    if responses is None:
        return redirect("/")
    if len(responses) == len(survey.questions):
        return redirect("/thanks")
    if question_id != len(responses):
        return redirect(f"/questions/{len(responses)}")
    
    questions = survey.questions[question_id].question
    choices = survey.questions[question_id].choices
    
    return render_template("question.html", questions=questions, question_num=question_id, choices=choices)

@app.route("/answer", methods=["POST"])
def answer():
    answer = request.form["answer"]
    
    responses = session[RESPONSES_KEY]
    responses.append(answer)
    session[RESPONSES_KEY] = responses
    if(len(responses) == len(survey.questions)):
        return redirect("/thanks")
    else:
        return redirect(f"/questions/{len(responses)}")



@app.route("/thanks")
def thanks():
    return render_template("thanks.html")