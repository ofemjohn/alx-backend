#!/usr/bin/env python3
'''using flask babel'''
from flask import Flask, request
from flask_babel import Babel, gettext
from flask import render_template


app = Flask(__name__)
babel = Babel(app)


class Config:
    '''babel configuration file'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    '''local selector'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''render templates for babel'''
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5009)
