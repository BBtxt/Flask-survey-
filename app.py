from flask import Flask, render_template
from surveys import satisfaction_survey as survey

app = Flask(__name__)


@app.route("/" )
def hello():
    return render_template("survey.html")

@app.route("/questions/<int:question_id>")
def questions(question_id):
    if question_id < 0 or question_id >= len(survey.questions):
        return render_template("invalid.html")
    
    questions = survey.questions[question_id].question
    choices = survey.questions[question_id].choices
    add_text = survey.questions[question_id].allow_text
    return render_template("question.html", questions=questions , choices=choices , add_text=add_text)