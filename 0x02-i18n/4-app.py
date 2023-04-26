#!/usr/bin/env python3
'''using flask babel'''
from flask import Flask, request
from flask_babel import Babel
from flask import render_template


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    '''Babel config'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def helloWorld() -> str:
    '''Render template '''
    return render_template('4-index.html')


@babel.localeselector
def get_locale() -> str:
    '''local'''
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
