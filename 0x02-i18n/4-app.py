#!/usr/bin/env python3
'''using flask babel'''
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    '''Babel config'''
    LANGUAGES = ['en', 'fr']


app.config.from_object(Config)
Babel.default_locale = 'en'
Babel.default_timezone = 'UTC'


@babel.localeselector
def get_locale():
    '''local'''
    locale = request.args.get("locale")
    if locale:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', methods=['GET'])
def index():
    '''route'''
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True, port='5009')
