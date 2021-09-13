from flask import Blueprint

business = Blueprint('business', __name__)

from app.controllers.business import businessController
