from asgiref.wsgi import WsgiToAsgi

from configparser import ConfigParser

configure = ConfigParser()
configure.read("./newrelic.ini")

from dotenv import load_dotenv

load_dotenv()

import os
from flask import Flask
from models.model import db
from blueprints.operations import operations_blueprint
from errors.errors import ApiError


if os.getenv("ENV") != "test":
    print("ENV: ", os.getenv("ENV"))
    print("DB_USER: ", os.getenv("DB_USER"))
    print("DB_PASSWORD: ", os.getenv("DB_PASSWORD"))
    print("DB_HOST: ", os.getenv("DB_HOST"))
    print("DB_PORT: ", os.getenv("DB_PORT"))
    print("DB_NAME: ", os.getenv("DB_NAME"))
    DATABASE = f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"
else:
    print("ENV: ", "No env")
    DATABASE = os.environ["DATABASE"]

application = Flask(__name__)

WsgiToAsgi(application)

application.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app_context = application.app_context()
app_context.push()

db.init_app(application)
db.create_all()


application.register_blueprint(operations_blueprint)


@application.errorhandler(ApiError)
def handle_exception(err):
    return "", err.code
