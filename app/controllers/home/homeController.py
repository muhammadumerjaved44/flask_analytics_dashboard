from flask import render_template
from flask_login import login_required
import json

from . import home
from app.models.sales_model import SalesMethods as sm


@home.route('/')
@login_required
def homepage():
    """
    Render the homepage template on the / route
    """

    totalNumberOfSales = sm.getAllNumberOfSales()
    allSales           = sm.getAllSales()
    salesByValue = sm.getAllSalesByValue()
    profit = sm.getProfit()
    geoCountriesCount = sm.geoCountriesCount()
    salesUnderwriter = sm.getSalesByUnderwriter()


    return render_template(
        'home/index.html',
        title = "Dashboard",
        totalNumberOfSales = totalNumberOfSales,
        timestamp          = list(allSales.get('datetime')),
        currCost           = list(allSales.get('currCost')),
        salesByValue=salesByValue,
        profit=profit,
        geoCountriesCount = json.dumps(geoCountriesCount),
        salesUnderwriter = json.dumps(salesUnderwriter),
        )


@home.route('/dashboard')
@login_required
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title = "Dashboard")
