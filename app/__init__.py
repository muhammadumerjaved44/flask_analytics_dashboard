# third-party imports
import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

# local imports
from config import app_config

BASE_PATH = os.path.dirname(os.path.dirname(__file__))

# class instencesses
login_manager = LoginManager()
db            = SQLAlchemy()
flaskCache    = Cache()

def create_app(config_name):
    """
    Args:
        config_name: development | production

    Returns: app

    author: Muhammad Umar Javed
    """
    global mainDB, geoDB

    app                = Flask(__name__, instance_relative_config = True)
    app._static_folder = os.path.join(BASE_PATH, 'app/static/')
    app.config.from_object(app_config.get('development'))
    # app.config. from_pyfile('config.py')
    Bootstrap(app)
    db.init_app(app)
    mainDB = db.get_engine(app = app, bind = 'maindb')
    geoDB  = db.get_engine(app = app, bind = 'geodb')
    flaskCache.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view    = "auth.login"
    migrate                     = Migrate(app, db)

    from app.models import models, sales_model, commission_details

    from app.controllers.admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix = '/admin')

    from app.controllers.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from app.controllers.home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from app.controllers.users import users as users_blueprint
    app.register_blueprint(users_blueprint)

    from app.controllers.business import business as business_blueprint
    app.register_blueprint(business_blueprint)

    return app
