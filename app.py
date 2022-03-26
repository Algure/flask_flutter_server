
from flask import Flask
from flask import send_from_directory
from flask import render_template


app = Flask(__name__, )
# app = Flask(__name__, template_folder='templates')

FLUTTER_WEB_APP = 'templates'


@app.route('/')
def render_page():
    return render_template('/index.html')


@app.route('/web/')
def render_page_web():
    return render_template('index.html')


@app.route('/web/<path:name>')
def flutter_redirect(name):

    dData = str(name).split('/')
    DIR_NAME = FLUTTER_WEB_APP

    if len(dData) > 1:
        for i in range(0, len(dData) - 1):
            DIR_NAME += '/' + dData[i]

    if ('#' in dData[-1] or dData[-1] == '#/' or dData[-1] == '#'):
        dData[-1] = 'index.html'

    return send_from_directory(DIR_NAME, dData[-1])


if __name__ == '__main__':
    app.run()

