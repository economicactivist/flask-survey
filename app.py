from flask import Flask, render_template, redirect, request
from flask.helpers import url_for
from surveys import satisfaction_survey
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

responses = []
num = 0  # variable to set page number


@app.route('/')
def index():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('index.html', title=title, instructions=instructions, num=num)


@app.route('/questions/<num>')
def questions(num):
    num = int(num)  # change string to integer
    if num < len(satisfaction_survey.questions):
        q = satisfaction_survey.questions[num]
        num += 1
        return render_template('questions.html', question=q.question, choices=q.choices, num=num)
    else:
        return '<body><h1>Thank You!</h1></body>'
# if __name__ == '__main__':
#   app.run(host='127.0.0.1', port=8000, debug=True)
@app.route('/answer/<num>', methods=['POST'])
def save_answer(num):
    answer= request.form
    responses.append(answer['answer'])
    print(responses)
    return redirect(url_for('questions', num=num))
