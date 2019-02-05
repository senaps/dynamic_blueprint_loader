from flask import Flask


def create_app():
    app = Flask(__name__)

    _load_blueprints(app)

    return app


def _load_blueprints(app):
    from .apps.test_app import test

    app.register_blueprint(test)