import os
from dotenv import load_dotenv

load_dotenv('.env')

class Config(object):
  TESTING = False

class ProductionConfig(Config):
  DATABASE_URI = os.environ['DATABASE_URI']

class DevelopmentConfig(Config):
  DATABASE_URI = os.environ['DATABASE_URI']

class TestingConfig(Config):
  DATABASE_URI = 'sqlite:///:memory:'
  TESTING = True
