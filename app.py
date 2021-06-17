from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
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
import os
from sqlite3 import Error
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
dbURI = 'sqlite:///models/DBreal.db'

''' database setup  '''
# project_dir = os.path.dirname(os.path.abspath(__file__))
# database_file = "sqlite:///{}".format(os.path.join(project_dir, "searching.db"))
# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = database_file


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

'''app secret key'''
app.secret_key = 'nighthawks'


class Search(db.Model):
    searchid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    menuitem = db.Column(db.String(255), unique=False, nullable=False)
    link = db.Column(db.String(255), unique=False, nullable=False)

    def __repr__(self):
        return '<Search %r>' % self.searchid


db.create_all()

''' table creation '''
db.create_all()

search = Search(menuitem="tweets", link="/createTweet")
search1 = Search(menuitem="tweet", link="/createTweet")
search2 = Search(menuitem="share", link="/share")
search3 = Search(menuitem="sign up", link="/signup")
search4 = Search(menuitem="login", link="/login")
search5 = Search(menuitem="home", link="/")
search6 = Search(menuitem="api", link="/api")
db.session.add(search)
db.session.add(search1)
db.session.add(search2)
db.session.add(search3)
db.session.add(search4)
db.session.add(search5)
db.session.add(search6)
db.session.commit()


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


@app.route('/createTweet', methods=["GET", "POST"])
def createTweet():
    # tweets = None
    # if request.form:
    # postdata = Tweet(tweetid=request.form.get("tweetid"), tweet=request.form.get("tweet"),
    # username=request.form.get("username"))
    # db.session.add(postdata)
    # db.session.commit()
    # tweets = Tweet.query.all()
    # print(tweets.count)
    if session.get("user_id") == None:
        return redirect("/login")
    if request.method == "POST":
        db.engine.execute(
            text("INSERT INTO tweet (tweetContent, user) VALUES (:tweet, :user);").execution_options(autocommit=True),
            tweet=request.form.get("tweet"),
            user=session["user_id"]
        )

        resultproxy = db.engine.execute(
            text("SELECT * FROM users WHERE id=:id;").execution_options(autocommit=True),
            id=session["user_id"]
        )
        user = convert(resultproxy)
        return redirect(url_for("userProfile", usr=user["username"]))
    else:
        return render_template("createTweet.html", tweets=tweets)


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


@app.route('/share', methods=['POST', 'GET'])
def share():
    return render_template("share.html")


@app.route("/<usr>")
def userProfileBad(usr):
    return redirect("/login")


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
        print(session)

        # redirects us to the user page
        return redirect(url_for("userProfile", usr=user["username"]))
    else:
        return render_template("login.html", error=False)


@app.route('/signup')
def signup():
    return redirect('/newuser/')


@app.route('/api')
def api():
    print("test")
    url = "https://pieceofthepi.nighthawkcodingsociety.com/Food/" + str(random.randint(1, 7))
    print(url)
    response = requests.request("GET", url)
    print(response)
    formatted = json.loads(response.text)
    return render_template("pizza.html", pizza=formatted)


@app.route("/profile")
def redirectProfile():
    try:
        resultproxy = db.engine.execute(
            text("SELECT * FROM users WHERE id=:id;").execution_options(autocommit=True),
            id=session["user_id"])
        user = convert(resultproxy)
        return redirect(url_for("userProfile", usr=user["username"]))
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
        return redirect('/login')
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

    # find out if it is the current user
    currentUser = False
    if session.get("user_id") == None:
        print("anonymous")
    else:
        if user["id"] == session["user_id"]:
            currentUser = True

    return render_template("profile.html", user=user, tweets=userTweets, currentUser=currentUser)


@app.route('/search_results', methods=["GET", "POST"])
def search_results():
    # function use Flask import (Jinja) to render an HTML template
    searchkey = None
    selectedsearch = None
    if request.form:
        searchkey = request.form.get("search")
        print(searchkey)
        selectedsearch = Search.query.filter_by(menuitem=searchkey).first()
        return render_template("searchresults.html", data=selectedsearch)
        # error=selectedsearch
    else:
        error = "Invalid Input. Please try again."
    # return redirect(url_for('landing_page'))
    return render_template("searchresults.html", error=error)


@app.route('/browse', methods=["GET"])
def browse():
    userTweets = db.engine.execute(text("SELECT * FROM tweet").execution_options(autocommit=True))
    userTweets = convertList(userTweets)
    users = db.engine.execute(text("SELECT * FROM users").execution_options(autocommit=True))
    users = convertList(users)
    return render_template("browse.html", tweets=userTweets, users=users)


@app.route('/apipull/tweets', methods=["GET", "POST"])
def apiPullTweets():
    userTweets = db.engine.execute(text("SELECT * FROM tweet").execution_options(autocommit=True))
    userTweets = convertList(userTweets)
    return jsonify(userTweets)


@app.route('/apipull/users', methods=["GET", "POST"])
def apiPullUsers():
    users = db.engine.execute(text("SELECT * FROM users").execution_options(autocommit=True))
    users = convertList(users)
    return jsonify(users)


@app.route('/api_form_POST', methods=["GET", "POST"])
def api_form_POST():
    if request.method == 'POST':
        # getting the information from the form
        restaurant = request.form.get('restaurant')
        name = request.form.get('name')
        star_count = request.form.get("star_count")
        message_input = request.form.get("message")

        # formatting information into the URL use to access the API
        url_info = 'https://pieceofthepi.nighthawkcodingsociety.com/createReview/' + str(restaurant) + "/" + str(
            name) + "/peasant/" + str(star_count) + '/' + str(message_input)
        print(url_info)

        # POST to the API
        requests.post(url_info)

        # render the default page
        return render_template('api_form_POST.html')

    return render_template('api_form_POST.html')


@app.route('/api_form_GET/<usr>', methods=["GET"])
def api_form_GET(usr):
    # compute rows
    resultproxy = db.engine.execute(
        text("SELECT * FROM users WHERE username=:username;").execution_options(autocommit=True),
        username=usr)

    user = convert(resultproxy)
    if user == False:
        return apology("invalid username", 403)

    # get the users playlists
    userTweets = db.engine.execute(
        text("SELECT * FROM tweet WHERE user=:user;").execution_options(autocommit=True),
        user=user["id"])
    userTweets = convertList(userTweets)
    print(userTweets)

    return jsonify(userTweets)


@app.route('/createTweetAPI/<user>/<content>', methods=["GET"])
def createTweetAPI(user, content):
    db.engine.execute(
        text("INSERT INTO tweet (tweetContent, user) VALUES (:tweet, :user);").execution_options(autocommit=True),
        tweet=content,
        user=user
    )
    return jsonify([user, content])


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(port='4000', host='127.0.0.1')
