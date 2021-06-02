from flask import Flask, render_template, redirect, request, flash, session
from flask.helpers import url_for
from surveys import satisfaction_survey
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

responses = []
page_num = 0  # variable to set page number


@app.route('/')
def index():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('index.html', title=title, instructions=instructions, num=page_num)

@app.route('/initialize-session', methods=['POST'])
def init_session(num):
    session["responses"] = []
    return redirect(url_for('questions', num=page_num))

@app.route('/questions/<num>')
def questions(num):
    global page_num
    input_num = int(num)
    if input_num != page_num:
        flash('You\'re trying to access an invalid question')
        return redirect(url_for('questions', num=page_num))
    page_num = int(num)  # change string to integer
    if page_num < len(satisfaction_survey.questions):
        q = satisfaction_survey.questions[page_num]

        return render_template('questions.html', question=q.question, choices=q.choices, num=page_num)
    else:
        return '<body><h1>Thank You!</h1></body>'
# if __name__ == '__main__':
#   app.run(host='127.0.0.1', port=8000, debug=True)


@app.route('/answer/<num>', methods=['POST'])
def save_answer(num):
    # global page_num += 1
    global page_num
    page_num += 1
    answer = request.form
    responses.append(answer['answer'])
    print(responses)
    print('num variable', num)
    print('page_num variable', page_num)

    return redirect(url_for('questions', num=num))
