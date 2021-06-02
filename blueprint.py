from flask import Blueprint

blueprint = Blueprint('blueprint', __name__)

# This is our flask blueprint
# it lays out how we would like our app to work, as long as dividing our work among our groupmates

@blueprint.route('/')
def index():
    return "This is our homepage. This will allow users to view the tweets of people you follow, similar to how the " \
           "regular Twitter homepage looks. Assigned to Noya."


@blueprint.route('/nav')
def createTweet():
    return "While this wont be a physical page, the navbar, at the top of each page, will include a link to the " \
           "user's profile, home, liked posts, create posts page and search bar. Assigned to Akhil"

@blueprint.route('/createTweet')
def createTweet():
    return "This is our create Tweets page. Assigned to Maggie"

@blueprint.route('/liked')
def liked():
    return "This page shows your liked tweets. Assigned to Noya."


@blueprint.route('/browse', methods=['POST', 'GET'])
def explore():
    return "This will allow you to browse all tweets, not only the ones of people you follow, which is seen on your " \
           "homepage. Assigned to Sarah."


@blueprint.route("/<usr>")
def userProfile(usr):
    return "This is will allow you to see the profiles of various users. It will be displayed differently if it is " \
           "detected that you own a specific profile. It will display your tweets, your followers, your bio, " \
           "and your profile picture. Assigned to Sarah."


@blueprint.route('/editProfile', methods=["GET", "POST"])
def editProfile():
    return "This will allow you to edit your profile. Assigned to Nivu. "


@blueprint.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        formUser = request.form["username"]
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
        return redirect(url_for("user1", usr=user["username"]))
    else:
        return render_template("login.html", error=False)


@blueprint.route('/signup')
def signup():
    return "Signup Here. Assigned to Nivu"