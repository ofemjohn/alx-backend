#!/usr/bin/env python3
'''using flask babel'''
from flask import Flask
from flask_babel import Babel
from flask import render_template


app = Flask(__name__)
babel = Babel(app)


class Config:
    '''babel configuration file'''
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)
BABEL_DEFAULT_LOCALE = 'en'
BABEL_DEFAULT_TIMEZONE = 'UTC'


@app.route('/')
def index():
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5009)
