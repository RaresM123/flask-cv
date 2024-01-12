import os

from flask import Flask
from flaskr.cache import cache
from flaskr.commands import cli_bp
from flaskr.routes import bp


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DEBUG=True,
        JSONIFY_PRETTYPRINT_REGULAR=True
    )

    app.register_blueprint(bp)
    app.register_blueprint(cli_bp)
    cache.init_app(app)
    return app
