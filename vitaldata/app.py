from flask import Flask, render_template
from flask_cors import CORS

from vitaldata import VitalData

app = Flask(__name__)
vital = VitalData()

CORS(app)
@app.route('/vital-data', methods = ["GET"])

def index():

    vital.update_vital()
    return vital.make_json()

if __name__ == '__main__':
    app.debug = True
    app.run()