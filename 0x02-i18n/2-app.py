#!/usr/bin/env python3
'''using flask babel'''
from flask import Flask, request
from flask_babel import Babel
from flask import render_template


app = Flask(__name__)
babel = Babel()
babel.init_app(app)


class Config:
    '''babel configuration file'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@staticmethod
def get_locale():
    '''config for languages'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''render templates for babel'''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5009)
