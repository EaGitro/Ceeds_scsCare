from flask import Flask, render_template
from vitaldata import VitalData

app = Flask(__name__)
vital = VitalData()

@app.route('/todo-data')
def index():

    vital.update_vital()
    return vital.make_json()

if __name__ == '__main__':
    app.debug = True
    app.run()