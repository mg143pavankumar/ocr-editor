from flask import Flask, send_from_directory, render_template, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS  #comment this on deployment
from mgodb.db import initialize_db
from api.routes import initialize_routes
from config.appconfig import Config
from flask_sqlalchemy import SQLAlchemy
import models
from models import initialize_db

app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)  #comment this on deployment
api = Api(app)

app.config['SANDHI_LIB_INPUT_DIR'] = 'C:/Users/HP/sandhi/input/'
app.config['SANDHI_LIB_OUTPUT_DIR'] = 'C:/Users/HP/sandhi/output/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['MONGODB_SETTINGS'] = {
#    'host': 'mongodb://127.0.0.1:27017/sandhi-books'
#}

#app.config.from_object(Config())

initialize_db(app)

initialize_routes(api)


@app.route("/cli", strict_slashes=False)
@app.route("/cli/pageview", strict_slashes=False)
def serve():
    return send_from_directory(app.static_folder, 'index.html')

