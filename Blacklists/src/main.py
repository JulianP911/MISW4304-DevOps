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

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_NAME']}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

app.register_blueprint(operations_blueprint)


@app.errorhandler(ApiError)
def handle_exception(err):
    return "", err.code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)