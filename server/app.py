from flask import Flask
from .models import db
from .routes import main as main_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    app.register_blueprint(main_blueprint)

    return app
