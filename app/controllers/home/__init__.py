from flask import Blueprint

home = Blueprint('home', __name__)

from app.controllers.home import homeController
