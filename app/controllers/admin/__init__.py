from flask import Blueprint

admin = Blueprint('admin', __name__)

from app.controllers.admin import adminController
