from flask import Flask, render_template, request
from flask_babel import Babel, get_locale


app = Flask(__name__)
babel = Babel(app)

@babel.localeselector
def localeselector():
    # return 'en_US'
    return request.accept_languages.best_match(['en', 'es', 'ru'])


@app.route('/')
def index():
    return f'<h1>Locale: {get_locale()}</h1>'


if __name__ == "__main__":
    app.run(debug=True)