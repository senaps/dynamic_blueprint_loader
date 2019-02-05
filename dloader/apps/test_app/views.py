from . import test


@test.route("/")
def index():
    return "hello world!"