from flask import Flask, render_template
from flask_cors import CORS

from vitaldata import VitalData

app = Flask(__name__)
vital = VitalData()

CORS(app)
@app.route('/vital-data', methods = ["GET"])
def vital_data():

    vital.update_vital()
    return vital.make_json()

@app.route('/', methods = ["GET"])
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.debug = True
    app.run()