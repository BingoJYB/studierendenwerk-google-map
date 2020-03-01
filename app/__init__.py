from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import import_string

extensions = [
    'app.models:db'
]
blueprints = [
    'app.routes:my_app'
]


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        for extension in extensions:
            ext = import_string(extension)
            ext.init_app(app)

            if isinstance(ext, SQLAlchemy):
                ext.create_all()

        for blueprint in blueprints:
            bp = import_string(blueprint)
            app.register_blueprint(bp)

        return app
