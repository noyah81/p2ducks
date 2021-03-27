from flask import Blueprint

blueprint = Blueprint('blueprint', __name__)


@blueprint.route('/')
def index():
    return "This is an example app"


@blueprint.route('/newpost')
def newpost():
    return render_template("newpost.html")