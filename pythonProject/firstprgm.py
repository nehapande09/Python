import flask
from flask import render_template

app = flask.Flask(__name__, static_folder='/', template_folder='/')


@app.route('/')
def index():
    # return "hello world"
    return render_template('index.html')


@app.route('/home')
def login():
    return "hello neha"
    # return render_template('index.html')


if __name__ == '__main__':
    app.run()
    app.debug = True
