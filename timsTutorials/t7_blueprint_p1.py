from flask import Flask, render_template
from t7_blueprint_p2 import part2

app = Flask(__name__)
app.register_blueprint(part2, url_prefix='')


@app.route('/')
def test():
    return '<h1>Test it!</h1>'



if __name__ == "__main__":
    app.run(debug=True)