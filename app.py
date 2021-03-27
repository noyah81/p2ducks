from flask import Flask
from blueprint import blueprint


app = Flask(__name__)
app.register_blueprint(blueprint)