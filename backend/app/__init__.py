from importlib import import_module

from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from .base import Base
from .conf import settings

app = Flask(__name__)
app.config.from_object("app.conf.settings")


def init_db(db, app):
    # Need to following to make sure models are
    # registered with the db.
    from .models import PersonalizationSettings, User  # noqa

    # init db with flask app instance now.
    db.init_app(app)


db = SQLAlchemy(model_class=Base)
init_db(db, app)
migrate = Migrate(app, db)

flask_api = Api(app)

# load API versions
for api_version in settings.API_VERSIONS:
    api_module = import_module(f"{settings.API_ROOT}.{api_version}.routes")
    if hasattr(api_module, "routes") and isinstance(api_module.routes, list):
        for route, resource in api_module.routes:
            flask_api.add_resource(resource, route)
