from flask import render_template
from flask_login import login_required
import json

from . import business
from app.models.sales_model import SalesMethods as sm


# print('my view', db.get_engine(app, 'maindb'))
@business.route('/business')
@login_required
def index():
    """
    Render the homepage template on the / route
    """

    # salesIDS = Sales.query.all()
    salesByValue = sm.getAllSalesByValue()
    profit = sm.getProfit()
    salesBy30 = sm.salesBy30Days()
    geoLocPreviousCost, geoLocCurrentCost = sm.geoMapCurrCost()
    listOfUW, salesByPreviousYear, salesByCurrentYear = sm.getSalesByUnderWriterLastYear()
    previousYearSales, currentYearSales = sm.saleCompareByYear()
    hccProductList, hccSalesPreviousYear, hccSalesCurrentYear = sm.getSalesByHCC()
    newCustomerCountPreviousYear, repeatCustomerCountPreviousYear, newCustomerCountCurrentYear, repeatCustomerCountCurrentYear = sm.newAndRepeatSalesCount()


    return render_template(
        'business/index.html',
        title="Business",
        salesByValue=salesByValue,
        profit=profit,
        salesBy30=salesBy30,
        geoLocPreviousCost = json.dumps(geoLocPreviousCost),
        geoLocCurrentCost = json.dumps(geoLocCurrentCost),
        previousYearSales = previousYearSales, currentYearSales = currentYearSales,
        listOfUW = json.dumps(listOfUW), salesByPreviousYear = salesByPreviousYear, salesByCurrentYear = salesByCurrentYear,
        hccProductList = json.dumps(hccProductList), hccSalesPreviousYear = hccSalesPreviousYear, hccSalesCurrentYear = hccSalesCurrentYear,
        newCustomerCountPreviousYear = newCustomerCountPreviousYear, repeatCustomerCountPreviousYear = repeatCustomerCountPreviousYear, newCustomerCountCurrentYear = newCustomerCountCurrentYear, repeatCustomerCountCurrentYear = repeatCustomerCountCurrentYear
        )