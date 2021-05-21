from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# import classes from blueprints

# import from blueprints
from templates.minilabs.sarah.sarah import sarah
#from templates.minilabs.maggie.maggie_minilab import maggie
from templates.minilabs.nivu.nivu import nivu
from templates.minilabs.akhil.akhil import akhil
from templates.minilabs.noya.noya import noya


app = Flask(__name__)

# register the blueprints
app.register_blueprint(sarah)
#app.register_blueprint(maggie)
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



    #repr is a representation of the object.
def __repr__(self):
        #f"..." is string formatting.
        return f"comment data: {self.tweet}"

db.create_all();
@app.route('/')
def index():
    return render_template("home.html")


@app.route('/createTweet')
def createTweet():
    return render_template("createTweet.html")


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
