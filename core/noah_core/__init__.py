import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from noah_core.blueprints.interactions import interactions_blueprint


def init_config(app, test_config):
  if test_config is None:
    # load the instance config, if it exists, when not testing
    # TODO: Need to account for prod env
    app.config.from_object('config.DevelopmentConfig')
  else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

def init_db(app):
  db = SQLAlchemy()
  app.config["SQLALCHEMY_DATABASE_URI"] = app.config["DATABASE_URI"]
  db.init_app(app)
  alembic = Alembic()
  alembic.init_app(app)

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)

  init_config(app, test_config)
  print(app.config)
  init_db(app)

  # ensure the instance folder exists
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  app.register_blueprint(interactions_blueprint())

  return app
