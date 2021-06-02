from flask import Flask, render_template, request, session, redirect,url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from custom import apology, convert, convertList
from sqlite3 import Error
import random
import requests
import json
# import classes from blueprints

# import from blueprints
from templates.minilabs.sarah.sarah import sarah
from templates.minilabs.maggie.maggie import maggie
from templates.minilabs.nivu.nivu import nivu
from templates.minilabs.akhil.akhil import akhil
from templates.minilabs.noya.noya import noya


app = Flask(__name__)

# register the blueprints
app.register_blueprint(sarah)
app.register_blueprint(maggie)
app.register_blueprint(nivu)
app.register_blueprint(akhil)
app.register_blueprint(noya)

# Set the SQL database
dbURI = 'sqlite:///models/myDB.db'

""" database setup to support db examples """
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)
# set up the session
app.secret_key = "According to all known laws of aviation, there is no way a bee should be able to fly."

db.create_all()

# create database for tweet display
@app.route('/')
def index():
    return render_template("home.html")

from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "\pythonsqlite.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()


def tweets(args):
    pass


@app.route('/createTweet', methods=['POST', 'GET'])
def createTweet():
    if request.method == "POST":

        db.engine.execute(
            text("INSERT INTO tweet (tweetContent, user) VALUES (:tweet, :user);").execution_options(
                autocommit=True),
            tweet=request.form.get("tweet"),
            user=session["user_id"])


        resultproxy = db.engine.execute(
            text("SELECT * FROM users WHERE id=:id;").execution_options(autocommit=True),
            id=session["user_id"])

        user = convert(resultproxy)

        return redirect(url_for("userProfile", usr=user["username"]))
    else:
        return render_template("createTweet.html")


@app.route('/liked', methods=['POST', 'GET'])
def liked():
    return render_template("liked.html")


@app.route('/newuser/', methods=["GET", "POST"])
def new_user():
    """Register user"""
    if request.method == "POST":
        # Make sure they put in their username
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Make sure they put in a password
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Make sure the passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords must match", 403)

        fullname = request.form.get("name")
        print(request.form.get("bio") == '')

        # Insert all the values into the database
        db.engine.execute(
            text("INSERT INTO users (username, hash, name, bio) VALUES (:user, :hash, :name, :bio);").execution_options(
                autocommit=True),
            user=request.form.get("username"),
            hash=generate_password_hash(request.form.get("password")),
            name=fullname, bio=request.form.get("bio"))

        return redirect("/login")
    else:
        return render_template("signup.html")


@app.route('/editProfile', methods=["GET", "POST"])
def editProfile():
    return render_template("editProfile.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        formUser = request.form["username"]  # using name as dictionary key
        resultproxy = db.engine.execute(
            text("SELECT * FROM users WHERE username=:username;").execution_options(autocommit=True),
            username=formUser)

        user = convert(resultproxy)

        # troubleshooting
        if user == False:
            return render_template("login.html", error=True)

        # set the user id
        session.clear()
        session["user_id"] = user["id"]

        # redirects us to the user page
        return redirect(url_for("userProfile", usr=user["username"]))
    else:
        return render_template("login.html", error=False)


@app.route('/signup')
def signup():
    return redirect('/newuser/')

@app.route('/api')
def api():
    url = "http://pieceofthepi.cf/Food/" + str(random.randint(1, 7))
    response = requests.request("GET", url)
    formatted = json.loads(response.text)
    print(formatted)
    return render_template("pizza.html", pizza=formatted)



@app.route("/profile")
def redirectProfile():
    try:
        resultproxy = db.engine.execute(
            text("SELECT * FROM users WHERE id=:id;").execution_options(autocommit=True),
            id=session["user_id"])
        user = convert(resultproxy)
    except:
        return redirect('/login')



@app.route("/profile/<usr>")
def userProfile(usr):
    # compute rows
    resultproxy = db.engine.execute(
        text("SELECT * FROM users WHERE username=:username;").execution_options(autocommit=True),
        username=usr)

    user = convert(resultproxy)
    if user["username"] == "noUser":
        user = {'id': 404, 'username': 'LOGIN',
                'hash': 'LOGIN',
                'name': 'LOGIN', 'bio': "LOGIN"}
    elif user == False:
        user = {'id': 404, 'username': 'iDontExist',
                'hash': 'password hash',
                'name': 'That user does not exist!', 'bio': "You probably typed a name in the search bar. The user "
                                                            "you searched for either doesn't exist or deleted their "
                                                            "account"}
    # get the users playlists
    userTweets = db.engine.execute(
        text("SELECT * FROM tweet WHERE user=:user;").execution_options(autocommit=True),
        user=user["id"])
    userTweets = convertList(userTweets)
    print(userTweets)
    print(userTweets == [])

    # find out if it is the current user
    currentUser = False
    if user["id"] == session["user_id"]:
        currentUser = True

    return render_template("profile.html", user=user, tweets=userTweets, currentUser=currentUser)




if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(port='4000', host='127.0.0.1')
