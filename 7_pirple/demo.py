from flask import Flask
import model

app = Flask(__name__)
app.config['SECRET_KEY'] = 'myVerySecretKey'




from views import *


if __name__ == "__main__":
    app.run(port=5000, debug=True)
