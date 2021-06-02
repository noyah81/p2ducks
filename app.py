from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, session

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

class Tweet(db.Model):
    tweetid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tweet = db.Column(db.String(255), unique=False, nullable=False)
    username = db.Column(db.String(255), unique=True, nullable=True) #change to false later

    def __repr__(self):
        return '<Tweet %r>' % self.tweetid

#repr is a representation of the object.
def __repr__(self):
        #f"..." is string formatting.
        return f"comment data: {self.tweet}"

db.create_all()
@app.route('/')
def index():
    return render_template("home.html")


@app.route('/createTweet', methods=["GET", "POST"])
def createTweet():
    tweets = None
    if request.form:
        postdata = Tweet(tweetid=request.form.get("tweetid"), tweet=request.form.get("tweet"),
                    username=request.form.get("username"))
        db.session.add(postdata)
        db.session.commit()
    tweets = Tweet.query.all()
    print(tweets.count)
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
