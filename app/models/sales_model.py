
# third-party imports
from flask_sqlalchemy import declarative_base
import pandas as pd
from cachetools import cached, TTLCache
from sqlalchemy.sql import text
from serialize import loads
from collections import namedtuple
from datetime import datetime


# local imports
from app import db
from app import flaskCache
from app import mainDB
from app import geoDB



# class declerations

# Construct a base class for declarative class definitions.
Base = declarative_base()
# LRU Cache implementation with per-item time-to-live (TTL) value.
cache = TTLCache(maxsize=100, ttl=60)

class Sales(db.Model):
    """
    Sales:
        Sales Model with base declarelation

    Args:
        db (SQLAlchemy): One is binding the instance to a very specific Flask application
        Base (declarative): Construct a base class for declarative class definitions

    Create an Sales table
    """

    __tablename__  = 'g1g_sales'
    __table_args__ = {'extend_existing': True}
    __bind_key__   = 'maindb'

    saleID                 =  db.Column(db.Integer, primary_key = True)
    customerID             =  db.Column(db.Integer, index = True )
    affID                  =  db.Column(db.Integer, index = True )
    productID              =  db.Column(db.Integer, index = True )
    productName            =  db.Column(db.String(255), nullable = False, )
    carrierID              =  db.Column(db.Integer, index = True )
    productGroup           =  db.Column(db.Integer, index = True )
    data                   =  db.Column(db.Text, nullable = False, )
    policyData             =  db.Column(db.Text, nullable = False, )
    user                   =  db.Column(db.String(255), nullable = False, )
    timestamp              =  db.Column(db.Integer, index = True )
    quoteID                =  db.Column(db.Integer, index = True )
    price                  =  db.Column(db.Float, index = True, nullable = False, )
    affGroupID             =  db.Column(db.Integer, index = True )
    producerID             =  db.Column(db.Integer, index = True )
    primary_age            =  db.Column(db.Integer, index = True )
    age_round              =  db.Column(db.Integer, index = True )
    deductible             =  db.Column(db.Integer, index = True )
    coverage               =  db.Column(db.Integer, index = True )
    purchaser              =  db.Column(db.String(255), index = True,  nullable = False, )
    purchaser_email        =  db.Column(db.String(255), index = True,  nullable = False, )
    purchaser_city         =  db.Column(db.String(255), index = True,  nullable = False, )
    purchaser_state        =  db.Column(db.String(255), index = True,  nullable = False, )
    purchaser_country      =  db.Column(db.String(255), index = True,  nullable = False, )
    purchaser_zip          =  db.Column(db.String(255), index = True,  nullable = False, )
    primary_name           =  db.Column(db.String(255), index = True,  nullable = False, )
    primary_city           =  db.Column(db.String(255), index = True,  nullable = False, )
    primary_state          =  db.Column(db.String(255), index = True,  nullable = False, )
    primary_country        =  db.Column(db.String(255), index = True,  nullable = False, )
    primary_zip            =  db.Column(db.String(255), index = True,  nullable = False, )
    gig_commission         =  db.Column(db.Float, index = True,  nullable = False )
    aff_commission         =  db.Column(db.Float, index = True,  nullable = False )
    duration               =  db.Column(db.Integer, index = True)
    className              =  db.Column(db.String(255), nullable = False, )
    hash                   =  db.Column(db.String(255), nullable = False, )
    policyNumber           =  db.Column(db.String(255), nullable = False, )
    policyCert             =  db.Column(db.String(255), nullable = False, )
    cardNo                 =  db.Column(db.String(255), nullable = False, )
    apiResult              =  db.Column(db.Text, nullable = False, )
    UUID                   =  db.Column(db.String(255), nullable = False, )
    ipAddress              =  db.Column(db.String(100), nullable = False, )
    promoCode              =  db.Column(db.String(30), nullable = False, )
    discountDeductedAmount =  db.Column(db.String(50), nullable = False, )
    promoPaidStatus        =  db.Column(db.SmallInteger, nullable = False, )
    paidStatus_timestamp   =  db.Column(db.Integer, nullable = False, )
    checkNumber            =  db.Column(db.String(50), nullable = False, )
    affiliateUniqueId      =  db.Column(db.String(200), nullable = False, )
    salePrice              =  db.Column(db.Float, index = True, nullable = False, )
    expirationDate         =  db.Column(db.Integer, nullable = False, )
    reminderDate           =  db.Column(db.Integer, nullable = False, )
    reminderState          =  db.Column(db.Integer, nullable = False, )
    cancel_status          =  db.Column(db.SmallInteger, nullable = False, )
    policy_type            =  db.Column(db.SmallInteger, nullable = False, )


class SalesMethods(Sales):
    """
    SalesMethods
        SalesMethods contains the all the function that relates to the Sales model are written here

    Args:
        Sales (Mode): Sales Model with base declarelation
    """
    @classmethod
    @cached(cache)
    def getAllNumberOfSales(Sales):
        """
        getAllNumberOfSales : get all the sales count representing the total of sales records

        Args:
            Sales (Model): Sales Model with base declarelation

        Returns:
            Int: totalNumberOfSales
        """
        totalNumberOfSales = Sales.query.count()
        return totalNumberOfSales

    @classmethod
    @flaskCache.cached(timeout=600)
    def getAllSales(Sales):
        """
        getAllSales : fetch all current cost group by months and years

        Args:
            Sales (Model): Sales Model with base declarelation

        Returns:
            dict: allSales
        """
        q = text('''
                SELECT SUM(currCost) AS 'currCost', datetime, month, year, timestamp
                FROM (
                    SELECT g1g_sales.saleID, g1g_sales.timestamp,
                    FROM_UNIXTIME(g1g_sales.timestamp,'%Y') AS 'year',
                    FROM_UNIXTIME(g1g_sales.timestamp,'%M') AS 'month',
                    TRIM('"' FROM SUBSTRING_INDEX(SUBSTRING_INDEX(g1g_sales.data, ';', 8), ':',-1)) AS 'currCost',
                    DATE_FORMAT(FROM_UNIXTIME(g1g_sales.timestamp),'%d/%M/%Y') AS 'datetime'
                    FROM
                    g1g_sales
                    ORDER by g1g_sales.timestamp ASC) as SalesData
                GROUP BY year, month
                ORDER BY timestamp ASC
                ''')
        conn = mainDB.connect()
        allSales = conn.execute(q).fetchall()
        conn.close()
        temp = pd.DataFrame(allSales, columns=allSales[0].keys(), index=None)
        allSales = dict(temp)

        return allSales

    @classmethod
    def getAllSalesByValue(Sales):
        """
        getAllSalesByValue : get the total cumulative sum of sales

        Args:
            Sales (Model): Sales Model with base declarelation

        Returns:
            float: salesByValue
        """
        q = text('''
                SELECT SUM(currCost) AS 'total_sales_value'
                From (
                SELECT
                TRIM('"' FROM SUBSTRING_INDEX(SUBSTRING_INDEX(g1g_sales.data, ';', 8), ':',-1)) AS 'currCost'
                FROM
                g1g_sales) as Sales
                 ''')
        conn = mainDB.connect()
        salesByValue = conn.execute(q).scalar()
        conn.close()

        return salesByValue

    @classmethod
    def getProfit(Sales):
        """
        getProfit : get the profit of G1G form SUM(individual sale * individual commission) = Profit

        Args:
            Sales (Model): Sales Model with base declarelation

        Returns:
            float: profit
        """
        q = text('''
                SELECT SUM(g1g_worth) as 'profit'
                FROM(
                    SELECT
                        g1g_sales.saleID,
                        g1g_sales.productID,
                        TRIM('"' FROM SUBSTRING_INDEX(SUBSTRING_INDEX(g1g_sales.data, ';', 8), ':',-1)) AS 'Actual Cost (From Data String)',
                        g1g_products_info.productID AS 'g1g_products_info.productID',
                        g1g_products_info.gigCommission AS 'g1g_products_info.gigCommission',
                        TRIM('"' FROM SUBSTRING_INDEX(SUBSTRING_INDEX(g1g_sales.data, ';', 8), ':',-1)) * g1g_products_info.gigCommission AS 'g1g_worth'
                    FROM
                        g1g_sales
                    LEFT JOIN g1g_products_info ON
                        g1g_sales.productID = g1g_products_info.productID
                    ) as Profit
                ''')

        conn = mainDB.connect()
        profit = conn.execute(q).scalar()
        conn.close()

        return profit

    @classmethod
    def salesBy30Days(Sales):
        """
        salesBy30Days : get sales of past 30 days

        Args:
            Sales (Model): Sales Model with base declarelation

        Returns:
            dict: salesBy30
        """
        q = text('''
                SELECT
                g1g_sales.timestamp,
                DATE_FORMAT(FROM_UNIXTIME(g1g_sales.timestamp),'%d/%M/%Y') AS 'datetime',
                TRIM('"' FROM SUBSTRING_INDEX(SUBSTRING_INDEX(g1g_sales.data, ';', 8), ':',-1)) AS 'currCost'
                FROM
                g1g_sales
                ORDER BY `g1g_sales`.`timestamp`  DESC
                ''')

        conn = mainDB.connect()
        salesBy30 = conn.execute(q).fetchall()
        conn.close()

        return salesBy30

    @classmethod
    def geoMapCurrCost(Sales):
        """
        geoMapCurrCost : Get the Country wise Sales

        Args:
            Sales (Model): Sales Model with base declarelation

        Returns:
            List : This function returs the list of list of countries abbreviation and there aggregated currCost
        """
        q = text('''
                 SELECT * From (SELECT g1g_sales.saleID,FROM_UNIXTIME(g1g_sales.timestamp,'%Y') AS 'year', g1g_sales.data FROM `g1g_sales`) as saleDataYearly WHERE saleDataYearly.year BETWEEN 2018 and 2019
                 ''')
        conn = mainDB.connect()
        results = conn.execute(q).fetchall()
        count = 0
        error = 0
        errorList = []
        countList = []
        salesList = []
        for salesID, year, Data in results:
            try:
                count = count + 1
                unData = loads(Data.encode(), fmt='phpserialize')
                year = year
                data = namedtuple("data", unData.keys())(*unData.values())
                country = data.billcountry
                currCost = data.currCost
                billSate = data.billstate
                salesList.append((salesID, year, country, currCost, billSate))
                countList.append(count)
            except ValueError as e:
                count = count + 1
                error = error + 1
                errorList.append((error, count, Data.encode(), e))
        conn.close()
        sales = pd.DataFrame(salesList, columns = ['salesID', 'year', 'countryID', 'currCost', 'billSate'])
        sales['currCost'] = sales['currCost'].apply(lambda x: float(x))
        sales['countryID'] = sales['countryID'].apply(lambda x: int(x))
        sales['year'] = sales['year'].apply(lambda x: int(x))
        yearlySales = sales.groupby(['countryID', 'year'], as_index=False)['currCost'].sum()
        q2 = text('''
                  SELECT * FROM `countries`
                  ''')
        conn2 = geoDB.connect()
        result = conn2.execute(q2)
        countries = pd.DataFrame(result.fetchall(), columns = result.keys())
        conn2.close()
        salesByCountries = yearlySales.merge(countries, on=['countryID'], how='left')
        salesByCountries.dropna(inplace=True)
        salesByCountries['abbr'] = salesByCountries['abbr'].str.lower()
        geoLocPreviousCost = salesByCountries[['abbr', 'currCost']][salesByCountries['year']== 2018].round(3).values.tolist()
        geoLocCurrentCost = salesByCountries[['abbr', 'currCost']][salesByCountries['year']== 2019].round(3).values.tolist()
        return geoLocPreviousCost, geoLocCurrentCost

    @classmethod
    def getSalesByUnderwriter(Sales):
        q = text('''
                    SELECT
                    SalesByUWTable.*,
                    `g1g_carriers`.`name`
                    FROM
                    (
                        SELECT
                        g1g_sales.saleID,
                        g1g_sales.carrierID,
                        g1g_sales.cancel_status,
                        Sum(TRIM('"'
                        FROM
                        SUBSTRING_INDEX(SUBSTRING_INDEX(g1g_sales.data, ';', 8), ':', - 1))) AS 'SalesbyUW'
                        FROM
                        g1g_sales
                        WHERE
                        g1g_sales.cancel_status = 0
                        GROUP BY
                        carrierID
                    )
                    as SalesByUWTable
                    LEFT JOIN
                        g1g_carriers
                        on g1g_carriers.carrierID = SalesByUWTable.carrierID
                 ''')
        conn = mainDB.connect()
        result = conn.execute(q)
        salesUW = pd.DataFrame(result.fetchall(), columns = result.keys())
        conn.close()
        salesUnderwriter = salesUW[['name', 'SalesbyUW']].values.tolist()
        return salesUnderwriter

    @classmethod
    def saleCompareByYear(Sales):
        """
        saleCompareByYear : get the sales of 2018 and 19 and compare their monthly sales

        Args:
            Sales (Model): Sales Model with base declarelation

        Returns:
            List: previousYearSales, currentYearSales
        """
        q = text("""
                SELECT
                Sum(currCost) AS 'sumCost',
                month,
                year,
                timestamp
                FROM
                (
                    SELECT
                    g1g_sales.saleID,
                    g1g_sales.timestamp,
                    From_unixtime(g1g_sales.timestamp, '%Y') AS 'year',
                    From_unixtime(g1g_sales.timestamp, '%M') AS 'month',
                    Trim('"'
                    FROM
                    Substring_index(Substring_index(g1g_sales.data, ';' , 8), ':', - 1)) AS 'currCost'
                    FROM
                    g1g_sales
                    WHERE
                    cancel_status = 0
                    ORDER BY
                    g1g_sales.timestamp ASC
                )
                AS SalesData
                WHERE
                year BETWEEN 2018 AND 2019
                GROUP BY
                year,
                month
                ORDER BY
                timestamp ASC
                """)
        conn = mainDB.connect()
        result = conn.execute(q)
        sales = pd.DataFrame(result.fetchall(), columns = result.keys())
        conn.close()
        sales = sales
        sales['sumCost'] = sales['sumCost'].round(3)
        salesByYear = sales[sales['year']=='2018'].merge(sales[sales['year']=='2019'], on=['month'], how='left').fillna(0)
        previousYearSales  = salesByYear['sumCost_x'].values.tolist()
        currentYearSales  = salesByYear['sumCost_y'].values.tolist()
        return previousYearSales, currentYearSales


    @classmethod
    def geoCountriesCount(Sales):
        """
        geoCountriesCount : Get the Country wise Sales

        Args:
            Sales (Model): Sales Model with base declarelation

        Returns:
            List : This function returs the list of list of countries abbreviation and there aggregated currCost
        """
        q = text('''
                 SELECT g1g_sales.saleID, g1g_sales.data FROM `g1g_sales`
                 ''')
        conn = mainDB.connect()
        results = conn.execute(q).fetchall()
        count = 0
        error = 0
        errorList = []
        countList = []
        salesList = []
        for salesID, Data in results:
            try:
                count = count + 1
                unData = loads(Data.encode(), fmt='phpserialize')
                data = namedtuple("data", unData.keys())(*unData.values())
                country = data.billcountry
                currCost = data.currCost
                billSate = data.billstate
                salesList.append((salesID, country, currCost, billSate))
                countList.append(count)
            except ValueError as e:
                count = count + 1
                error = error + 1
                errorList.append((error, count, Data.encode(), e))
        conn.close()
        sales = pd.DataFrame(salesList, columns = ['salesID', 'countryID', 'currCost', 'billSate'])
        sales['currCost'] = sales['currCost'].apply(lambda x: float(x))
        sales['countryID'] = sales['countryID'].apply(lambda x: int(x))
        salesByCountriesCount = sales.groupby('countryID', as_index=False)['currCost'].count()
        q2 = text('''
                  SELECT * FROM `countries`
                  ''')
        conn2 = geoDB.connect()
        result = conn2.execute(q2)
        countries = pd.DataFrame(result.fetchall(), columns = result.keys())
        conn2.close()
        salesByCountries = salesByCountriesCount.merge(countries, on=['countryID'], how='left')
        salesByCountries.dropna(inplace=True)
        salesByCountries['abbr'] = salesByCountries['abbr'].str.lower()
        geoCountriesCount = salesByCountries[['abbr', 'currCost']].round(3).values.tolist()
        return geoCountriesCount

    @classmethod
    def getSalesByUnderWriterLastYear(Sales):
        """
        getSalesByUnderWriterLastYear : Get the sales by Under writers for year 2018 and 2019

        Args:
            Sales (Model): Sales Model with base declarelation

        Returns:
            List : listOfUW, salesByPreviousYear, salesByCurrentYear
        """

        q = text('''
                    SELECT
                    UnderWriterSales.*,
                    `g1g_carriers`.`name`
                    FROM
                    (
                        SELECT
                        Sales.*,
                        Sum(Sales.SalesbyUW) as 'currSum'
                        FROM
                        (
                            SELECT
                            g1g_sales.saleID,
                            g1g_sales.carrierID,
                            g1g_sales.cancel_status,
                            From_unixtime(g1g_sales.timestamp, '%Y') AS 'year',
                            TRIM( '"'
                            FROM
                            SUBSTRING_INDEX( SUBSTRING_INDEX(g1g_sales.data, ';', 8), ':', - 1 ) ) AS 'SalesbyUW'
                            FROM
                            g1g_sales
                        )
                        as Sales
                        WHERE
                        Sales.cancel_status = 0
                        and Sales.year BETWEEN 2018 and 2019
                        GROUP by
                        Sales.carrierID,
                        Sales.year
                        ORDER BY
                        `year` ASC
                    )
                    as UnderWriterSales
                    LEFT JOIN
                        g1g_carriers
                        on g1g_carriers.carrierID = UnderWriterSales.carrierID
                    ORDER BY
                    `UnderWriterSales`.`year` ASC
                 ''')
        conn = mainDB.connect()
        result = conn.execute(q)
        salesUW = pd.DataFrame(result.fetchall(), columns = result.keys())
        conn.close()
        salesUW = salesUW
        listOfUW = salesUW['name'].unique().tolist()
        sales = salesUW[salesUW['year']=='2018'].merge(salesUW[salesUW['year']=='2019'], on=['carrierID'], how='left').fillna(0)
        salesByPreviousYear = sales['currSum_x'].round(3).values.tolist()
        salesByCurrentYear = sales['currSum_y'].round(3).values.tolist()
        return listOfUW, salesByPreviousYear, salesByCurrentYear

    @classmethod
    def getSalesByHCC(Sales):
        """
        getSalesbyHCC : Get the sales by Product for HCC for year 2018 and 2019

        Args:
            Sales (Model): Sales Model with base declarelation

        Returns:
            List : hccProductList, hccSalesPreviousYear, hccSalesCurrentYear
        """
        q = text('''
                SELECT
                hccSales.*,
                g1g_carriers.name,
                SUM(hccSales.currCost) as 'sumCost'
                FROM
                (
                    SELECT
                    *
                    FROM
                    (
                        SELECT
                        g1g_sales.saleID,
                        g1g_sales.productName,
                        g1g_sales.carrierID,
                        From_unixtime(g1g_sales.timestamp, '%Y') AS 'year',
                        TRIM('"'
                        FROM
                        SUBSTRING_INDEX(SUBSTRING_INDEX(g1g_sales.data, ';', 8), ':', - 1)) AS 'currCost'
                        FROM
                        `g1g_sales`
                    )
                    as Sales
                    WHERE
                    Sales.carrierID = 1
                    and Sales.year BETWEEN 2018 and 2019
                    ORDER BY
                    `Sales`.`year` ASC
                )
                as hccSales
                LEFT JOIN
                    g1g_carriers
                    on g1g_carriers.carrierID = hccSales.carrierID
                GROUP by
                hccSales.productName
                ORDER BY
                `year` ASC
                ''')
        conn = mainDB.connect()
        result = conn.execute(q)
        sales = pd.DataFrame(result.fetchall(), columns = result.keys())
        conn.close()
        sales = sales
        salesHCC = sales[sales['year']=='2018'].merge(sales[sales['year']=='2019'], on=['productName'], how='outer').fillna(0)
        hccProductList = salesHCC.productName.tolist()
        hccSalesPreviousYear = salesHCC['currCost_x'].apply(lambda x: float(x)).round(3).values.tolist()
        hccSalesCurrentYear = salesHCC['currCost_y'].apply(lambda x: float(x)).round(3).values.tolist()
        return hccProductList, hccSalesPreviousYear, hccSalesCurrentYear

    @classmethod
    def newAndRepeatSalesCount(Sales):
        """
        newAndRepeatSalesCount : Get the repeat and new sales of 2018

        Args:
            Sales (Model): Sales Model with base declarelation

        Returns:
            List : newSalesCount, repeatSalesCount
        """
        monthList = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        monthListPd = pd.DataFrame(monthList, columns=['month'])
        q = text('''
                SELECT
                *
                From
                (
                    SELECT
                    g1g_sales.saleID,
                    g1g_sales.timestamp,
                    FROM_UNIXTIME(g1g_sales.timestamp, '%d') AS 'day',
                    FROM_UNIXTIME(g1g_sales.timestamp, '%Y') AS 'year',
                    From_unixtime(g1g_sales.timestamp, '%M') AS 'month',
                    g1g_sales.data
                    FROM
                    `g1g_sales`
                )
                as saleDataYearly
                WHERE
                saleDataYearly.year BETWEEN 2018 and 2019
                ''')
        conn = mainDB.connect()
        results = conn.execute(q).fetchall()
        count = 0
        error = 0
        errorList = []
        countList = []
        salesList = []
        for salesID, timestamp, day, year, month, Data in results:
            try:
                count = count + 1
                unData = loads(Data.encode(), fmt='phpserialize')
                data = namedtuple("data", unData.keys())(*unData.values())
                email = data.email
                currCost = data.currCost
                # tripStart = data.tripStart
                # tripEnd = data.tripEnd
                salesList.append((salesID, timestamp, day, year, month, email, currCost))
                countList.append(count)
            except ValueError as e:
                count = count + 1
                error = error + 1
                errorList.append((error, count, e))
        conn.close()
        salesList = salesList
        sales = pd.DataFrame(salesList, columns = ['salesID', 'timestamp', 'day', 'year', 'month', 'email','currCost'])
        sales['currCost'] = sales['currCost'].apply(lambda x: float(x))
        #  Pre processing steps
        sales['year'] = sales['year'].apply(lambda x: int(x))
        sales['email'] = sales['email'].str.lower()
        salesTwentyEighteen = sales[sales['year']==2018]
        salesTwentyNineteen = sales[sales['year']==2019]

        def preProcessing(salesYear):
            sortedSalesWithLessTime = salesYear.sort_values('timestamp', ascending=True)
            uniqueSales = sortedSalesWithLessTime[~sortedSalesWithLessTime.email.duplicated()]
            duplicateSales =  sortedSalesWithLessTime[sortedSalesWithLessTime.email.duplicated()]
            joinSales = uniqueSales[['salesID','month', 'email','currCost']].\
                merge(duplicateSales[['salesID', 'month', 'email','currCost']],
                    on=['email'], how='left')
            newUniqueSales = joinSales[~joinSales.email.duplicated()]
            newSales = newUniqueSales[['month_x', 'email', 'currCost_x']].groupby(['month_x'])['currCost_x'].count() #.reindex(monthList, axis=1).fillna(0).round(3)
            repeatSales = joinSales[['month_y', 'email', 'currCost_y']].groupby(['month_y'])['currCost_y'].count() #.reindex(monthList, axis=1).fillna(0).round(3)
            newSales.index.name,  repeatSales.index.name= 'month', 'month'
            newSalesCount = monthListPd.merge(newSales, on ='month', how='left').fillna(0).round(3)['currCost_x'].tolist()
            repeatSalesCount = monthListPd.merge(repeatSales, on ='month', how='left').fillna(0).round(3)['currCost_y'].tolist()
            return newSalesCount, repeatSalesCount
        newCustomerCountPreviousYear, repeatCustomerCountPreviousYear= preProcessing(salesTwentyEighteen)
        newCustomerCountCurrentYear, repeatCustomerCountCurrentYear = preProcessing(salesTwentyNineteen)
        return newCustomerCountPreviousYear, repeatCustomerCountPreviousYear, newCustomerCountCurrentYear, repeatCustomerCountCurrentYear










