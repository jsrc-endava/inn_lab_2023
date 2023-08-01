import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from noah_core.blueprints.interactions import interactions_blueprint
from authlib.integrations.flask_client import OAuth


def init_test_config(app, test_config):
  if test_config is None:
    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
  else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

def init_db(app):
  db = SQLAlchemy()
  app = Flask(__name__)
  app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
  db.init_app(app)

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'noah_core.sqlite'),
  )

  init_test_config(app, test_config)
  init_db(app)

  # ensure the instance folder exists
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  app.register_blueprint(interactions_blueprint())

  return app
