from flask import Blueprint


test = Blueprint('test', __name__)

from . import views

blueprint = test  # expose the blueprint to dynamic loader
# url_prefix = `/test`