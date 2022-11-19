import pytest
from flask import Flask


# This file contains config for tests.  Fixtures are just decorators, wrappers for your test functions that run before and after.

@pytest.fixture(scope="session")
def app():
    app = Flask(__name__)
    # other setup can go here
    app.testing = True

    yield app

    # clean up / reset resources here

@pytest.fixture(scope="session")
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()