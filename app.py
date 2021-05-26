from flask import Flask, render_template, redirect, templating
from surveys import satisfaction_survey
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
toolbar = DebugToolbarExtension(app)

responses = []
num = 0


@app.route('/')
def index():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('index.html', title=title, instructions=instructions, num=num)


@app.route('/questions/<num>')
def questions(num):
    num = int(num)
    if num < len(satisfaction_survey.questions):
        q = satisfaction_survey.questions[num]
        num += 1
        return render_template('questions.html', question=q.question, num=num)
    else:
        return '<h1>Thank You!</h1>'
# if __name__ == '__main__':
#   app.run(host='127.0.0.1', port=8000, debug=True)
