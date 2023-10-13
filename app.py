from datetime import datetime
from flask import Flask, render_template ,request, redirect
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from vitaldata import VitalData

import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)
vital = VitalData()
#db
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    detail = db.Column(db.String(100))
    due = db.Column(db.DateTime, nullable=False)
    is_archived = db.Column(db.Boolean, nullable=False)

# class TaskNumber(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     all_task_num = db.Column(db.Integer,nullable=False)
#     now_task_num = db.Column(db.Integer,nullable=False)

#-----------------

"""
{"all_task_num":0, "now_task":0}
"""

def read_file(path):
    f = open(path, mode = "r")
    data = f.read()
    f.close()
    return data


def write_file(path, content):
    f = open(path, mode="w")
    f.write(content)
    f.close()



class OperateJson:
    def __init__(self) -> None:
        write_file("./task_num.json", '{"all_task_num":0, "now_task":0}') 
        self.data = '{"all_task_num":0, "now_task":0}'
    def create_task(self):
        json_data = read_file("./task_num.json")
        obj_data = json.loads(json_data)
        obj_data["all_task_num"] += 1
        obj_data["now_task"] += 1
        json_data = json.dumps(obj_data)
        self.data = json_data
        write_file("./task_num.json",json_data)

    def delete_task(self, is_now):
        json_data = read_file("./task_num.json")
        obj_data = json.loads(json_data)
        obj_data["all_task_num"] -= 1
        if is_now :
            obj_data["now_task"] -= 1
        json_data = json.dumps(obj_data)
        self.data = json_data
        write_file("./task_num.json",json_data)

    def archive_task(self):
        json_data = read_file("./task_num.json")
        obj_data = json.loads(json_data)
        obj_data["now_task"] -= 1
        json_data = json.dumps(obj_data)
        self.data = json_data
        write_file("./task_num.json",json_data)

    def return_task(self):
        json_data = read_file("./task_num.json")
        obj_data = json.loads(json_data)
        obj_data["now_task"] += 1
        json_data = json.dumps(obj_data)
        self.data = json_data
        write_file("./task_num.json",json_data)
    
    def get_json(self):
        return self.data
#-----------------
operate_json = OperateJson()


@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if request.method == 'GET':
        posts_tmp = Post.query.all()
        # print(posts)
        # print(posts[0].id)
        posts = []
        archiveds = []
        for post in posts_tmp:
            if post.is_archived == False:
                posts.append(post)
            else :
                archiveds.append(post)

        return render_template('todo_index.html', posts=posts, archiveds=archiveds)

    else:
        title = request.form.get('title')
        detail = request.form.get('detail')
        due = request.form.get('due')
        is_archived = False

        due = datetime.strptime(due, '%Y-%m-%d')
        new_post = Post(title=title, detail=detail, due=due, is_archived=is_archived)
        operate_json.create_task()

        db.session.add(new_post)
        db.session.commit()
        return redirect('/todo')


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/detail/<int:id>')
def read(id):
    post = Post.query.get(id)

    return render_template('detail.html', post=post)

@app.route('/delete/<int:id>')
def delete(id):
    post = Post.query.get(id)
    if post.is_archived == False:
        operate_json.delete_task(True)
    else:
        operate_json.delete_task(False)

    db.session.delete(post)
    db.session.commit()
    return redirect('/todo')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    post = Post.query.get(id)
    if request.method == 'GET':
        return render_template('update.html', post=post)
    else:
        post.title = request.form.get('title')
        post.detail = request.form.get('detail')
        post.due = datetime.strptime(request.form.get('due'), '%Y-%m-%d')

        db.session.commit()
        return redirect('/todo')


@app.route('/move-to-archive/<int:id>', methods=["GET"])
def move_to_archive(id):
    post = Post.query.get(id)
    post.is_archived = True
    db.session.commit()
    operate_json.archive_task()

    return redirect("/todo")


@app.route('/return-to-post/<int:id>', methods=["GET"])
def return_to_post(id):
    post = Post.query.get(id)
    post.is_archived = False
    db.session.commit()
    operate_json.return_task()

    return redirect("/todo") 

@app.route("/get-tasknum-json",methods=["GET"])
def get_tasknum_json():
    return operate_json.get_json()

#db_end


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