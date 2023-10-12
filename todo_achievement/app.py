from flask import Flask, render_template
from todo_achievement_1 import todo

app = Flask(__name__)
ToDo = todo()

@app.route('/todo-data')
def index():

    ToDo.update_prob()
    return ToDo.make_json()

if __name__ == '__main__':
    app.debug = True
    app.run()