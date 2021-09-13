from flask import Blueprint

auth = Blueprint('auth', __name__)

from app.controllers.auth import authController
#from flask_app.app.auth import views
#import views