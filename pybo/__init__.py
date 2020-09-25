from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_pybo():
#     return 'Hello, Pybo!'

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()




def create_app():
    app = Flask(__name__)

    # @app.route('/')
    # def hello_pybo():
    #     return "hello, Pybo!"

    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models

    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    #필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app

