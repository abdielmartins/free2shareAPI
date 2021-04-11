from flask import Flask
from os import getenv

from config import config_selector

from free_2_share.configurations import database
from free_2_share.configurations import migration
from free_2_share.configurations import serializer

from free_2_share import views


def create_app():
    app = Flask(__name__)
    config_type = getenv("FLASK_ENV")
    app.config.from_object(config_selector[config_type])
    database.init_app(app)
    migration.init_app(app)
    serializer.init_app(app)
    views.init_app(app)

    return app