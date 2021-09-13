from flask import render_template
from flask_login import login_required, current_user

from . import users
from app import db
from app.models.models import Employee
from app import flaskCache


@users.route('/users')
@login_required
def index():
    """
    Render the homepage template on the / route
    """

    # salesIDS = Sales.query.all()
    employees = Employee.query.all()

    print(employees)

    if current_user.is_authenticated:
        print('this is current use ', current_user.id, current_user.first_name)


    return render_template(
        'users/index.html',
        title = "Users",
        employees = employees
        )

