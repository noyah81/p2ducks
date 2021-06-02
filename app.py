from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, session
import sqlite3
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


@app.route('/createTweet', methods=["GET", "POST"])
def createTweet():
    #tweets = None
    #if request.form:
        #postdata = Tweet(tweetid=request.form.get("tweetid"), tweet=request.form.get("tweet"),
                    #username=request.form.get("username"))
        #db.session.add(postdata)
        #db.session.commit()
    #tweets = Tweet.query.all()
    #print(tweets.count)
    return render_template("createTweet.html", tweets=tweets)


@app.route('/liked', methods=['POST', 'GET'])
def liked():
    return render_template("liked.html")


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
    app.run(port='4000', host='127.0.0.1')
