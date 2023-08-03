import os
from flask import Flask
from noah_core.extensions import db, migrate
from noah_core.blueprints.interactions import interactions_blueprint
from noah_core.blueprints.slack import slack_blueprint


def init_config(app, test_config):
  if test_config is None:
    # load the instance config, if it exists, when not testing
    # TODO: Need to account for prod env
    app.config.from_object('config.DevelopmentConfig')
  else:
    # load the test config if passed in
    app.config.from_mapping(test_config)

def init_db(app):
  app.config["SQLALCHEMY_DATABASE_URI"] = app.config["DATABASE_URI"]
  db.init_app(app)
  migrate.init_app(app, db)

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)

  init_config(app, test_config)
  init_db(app)

  # ensure the instance folder exists
  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass

  app.register_blueprint(interactions_blueprint())
  app.register_blueprint(slack_blueprint())

  return app
