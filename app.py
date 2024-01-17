from flask import Flask, render_template
from surveys import satisfaction_survey as survey

app = Flask(__name__)


@app.route("/" , methods=["POST"])
def hello():
    
    responses = []
    
    return render_template("survey.html", responses=responses)

@app.route("/questions/<int:question_id>")
def questions(question_id):
    if question_id < 0 or question_id >= len(survey.questions):
        return render_template("invalid.html")
    
    questions = survey.questions[question_id].question
    
    return render_template("question.html", question=questions)