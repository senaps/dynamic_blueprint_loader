import importlib
import os

from flask import Flask


def create_app():
    app = Flask(__name__)

    _load_blueprints(app)

    return app


def _load_blueprints(app):
    """dynamically load applications

    this function will load all the blueprints specified by name convention of
    `*_app` and registers them in the app.
    """
    folder_names =  os.listdir("dloader/apps/")
    for name in folder_names:
        if name.endswith("_app"):
            tmp_blueprint = importlib.import_module(f".{name}", "dloader.apps")
            # if tmp_blueprint.url_prefix:
            #    app.register_blueprint(tmp_blueprint.blueprint,
            #                           url_prefix=tmp_blueprint.url_prefix)
            app.register_blueprint(tmp_blueprint.blueprint)