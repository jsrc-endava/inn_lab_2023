import pytest
from flask_migrate import upgrade as flask_migrate_upgrade
from noah_core import create_app, db as _db

@pytest.fixture(scope="session")
def app():
  app = create_app(test_config={
    'TESTING': True,
    'DEBUG': True,
    'DATABASE_URI': 'sqlite:///:memory:'
  })
  with app.app_context():
    yield app

@pytest.fixture(scope="session")
def db(app, request):
  """Session-wide test database."""
  def teardown():
      _db.drop_all()

  _db.app = app

  flask_migrate_upgrade(directory="migrations")
  request.addfinalizer(teardown)
  return _db

@pytest.fixture(scope="function")
def session(db, request):
  def commit():
    db.session.flush()

  def teardown():
    db.session.rollback()
    db.session.close()
    db.session.commit = old_commit

  db.session.begin_nested()

  # patch commit method
  old_commit = db.session.commit
  db.session.commit = commit

  request.addfinalizer(teardown)
  return db.session
