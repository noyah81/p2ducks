from flask import Flask, flash, jsonify, redirect, url_for, render_template, request, session, current_app, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash
from blueprint import blueprint


app = Flask(__name__)
app.register_blueprint(blueprint)

# Set the SQL database
dbURI = 'sqlite:///models/myDB.db'

""" database setup to support db examples """
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

# set up the session
app.secret_key = "According to all known laws of aviation, there is no way a bee should be able to fly."


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/createTweet')
def createTweet():
    return render_template("createTweet.html")


@app.route('/explore', methods=['POST', 'GET'])
def explore():
    return render_template("explore.html")


@app.route("/<usr>")
def userProfile(usr):
    return render_template("profile.html")


@app.route('/editProfile', methods=["GET", "POST"])
def editProfile():
    return render_template("editProfile.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/signup')
def signup():
    return render_template("signup.html")


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(port='3000', host='127.0.0.1')
