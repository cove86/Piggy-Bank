import os

from flask import Flask, render_template
from . import db
from . import auth
from . import bank


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'pbank.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # # a simple page that says hello
    # @app.route('/hello')
    # def hello():
    #     return render_template('base.html')

    db.init_app(app)

    app.register_blueprint(auth.bp)

    app.register_blueprint(bank.bp)
    app.add_url_rule('/', endpoint='index')
    return app