from flask import Flask, render_template, redirect, request

from surveys import satisfaction_survey as survey

app = Flask(__name__)

responses = []
@app.route("/" )
def hello():
    title = survey.title
    return render_template("survey.html", title=title)

@app.route("/begin", methods=["POST"])
def start():
    responses.clear()
    return redirect("/questions/0")

@app.route("/questions/<int:question_id>")
def questions(question_id):
    
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
    responses.append(answer)
    if(len(responses) == len(survey.questions)):
        return redirect("/thanks")
    else:
        return redirect(f"/questions/{len(responses)}")



@app.route("/thanks")
def thanks():
    return render_template("thanks.html")