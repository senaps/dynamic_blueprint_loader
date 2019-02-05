import importlib
import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    _load_blueprints(app)

    return app


def _load_blueprints(app):
    folder_names =  os.listdir("dloader/apps/")
    for name in folder_names:
        if name.endswith("_app"):
            tmp_blueprint = importlib.import_module(f".{name}", "dloader.apps")
            app.register_blueprint(tmp_blueprint.blueprint)