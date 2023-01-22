import flask
from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from werkzeug.utils import redirect
from leaderboard import Leaderboard
from os import environ
import uuid


DEFAULT_ROUTE_LEADERBOARD = "index"
DEFAULT_ROUTE_PLAYER = "player"

app = Flask(__name__)
Bootstrap(app)

file = 'data.json'

# conn_string = environ.get("DB_URI")
leaderboard = Leaderboard()

@app.route("/")
def index():

    scores = leaderboard.get_scores()
    return render_template("index.html",
                            scores=scores)

@app.route("/player", methods=["GET", "POST"])
def player():
    if flask.request.method == "POST":
        id = str(uuid.uuid4())
        avatar = flask.request.values.get("avatar")
        playername = flask.request.values.get("playername")
        points = flask.request.values.get("points")
        leaderboard.add_score(
            {"id" : id, "avatar" : avatar, "playername" : playername, "points":points}
        )

        return redirect(url_for(DEFAULT_ROUTE_LEADERBOARD))
    else:
        avatars = leaderboard.get_avatar_dic()
        score = leaderboard.get_scores()
        return render_template("player.html", score = score, avatars = avatars)

#foqzEAYMR44iodg_2Nuu0w
#postgresql://revanth:foqzEAYMR44iodg_2Nuu0w@curly-bear-8326.7tt.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full	