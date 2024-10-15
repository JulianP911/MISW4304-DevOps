from dotenv import load_dotenv

load_dotenv()

import os
from flask import Flask
if os.getenv('ENV') == 'test':
    from .models.model import db
    from .blueprints.operations import operations_blueprint
    from .errors.errors import ApiError
else:
    from models.model import db
    from blueprints.operations import operations_blueprint
    from errors.errors import ApiError

application = Flask(__name__)

application.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"
)
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app_context = application.app_context()
app_context.push()

db.init_app(application)
db.create_all()

application.register_blueprint(operations_blueprint)


@application.errorhandler(ApiError)
def handle_exception(err):
    return "", err.code


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=3000)