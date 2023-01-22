import flask
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect
from readScheduleImage import getDataFromImg
from students import Students
from os import environ
import uuid
from time import sleep

DEFAULT_ROUTE_LEADERBOARD = "index"
DEFAULT_ROUTE_PLAYER = "viewSchedulee"

app = Flask(__name__)
Bootstrap(app)

file = 'data.json'

# conn_string = environ.get("DB_URI")
students = Students()

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/index.html")
def index1():
    return render_template("index.html")
@app.route("/upload.html")
def upload1sadas():
    return render_template("upload.html")
@app.route("/logIn.html")
def logIn():
    return render_template("logIn.html")
@app.route("/viewSchedule", methods=["GET"])
def viewSchedulee():
    return render_template("viewSchedule.html")
@app.route("/uploadImg", methods=["POST"])
def getImg():
    if flask.request.method == "POST":
        img = flask.request.files['file']
        #if schedule1.png doesn't exist, create it
        img.save('uploadedImages/schedule1.png')
        student = getDataFromImg("schedule1.png")
        print(student)
        #students.add_student(student)
        return redirect(url_for(DEFAULT_ROUTE_PLAYER))
    else:
        return redirect(url_for(DEFAULT_ROUTE_PLAYER))
# @app.route("/student", methods=["GET", "POST"])
# def player():
#     if flask.request.method == "POST":
#         # refers to modifying a student's preferences
#         email = flask.request.values.get("email")
#         if not students.get_student_email(email):
#             return redirect(url_for(DEFAULT_ROUTE_PLAYER))
#         classnum_to_change = flask.request.values.get("classnum")
#         for clas in students.get_student_email(email)['classes']:
#             if clas['classnum'] == classnum_to_change:
#                 preference = flask.request.values.get("Want Study Buddy?")


#         return redirect(url_for(DEFAULT_ROUTE_LEADERBOARD))
#     else:
#         avatars = students.get_avatar_dic()
#         score = students.get_scores()
#         return render_template("student.html", score = score, avatars = avatars)

#foqzEAYMR44iodg_2Nuu0w
#postgresql://revanth:foqzEAYMR44iodg_2Nuu0w@curly-bear-8326.7tt.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full	