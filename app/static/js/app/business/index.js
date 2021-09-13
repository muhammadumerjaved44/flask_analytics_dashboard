$(function () {

    /*
    """
     Function : Display the Countries wise Aggregated Current Cost 2019

      Returns:
          [type]: None
      """
      */

    var geoLocCurrentCost = $('div#geoLocCurrentCost').data('geoloccurrentcost');

    // Create the chart
    Highcharts.mapChart('geoLocCurrentCost', {
        chart: {
            map: 'custom/world'
        },

        title: {
            text: 'Per Country Revenue 2019'
        },

        subtitle: {
            text: 'Source map: <a href="http://code.highcharts.com/mapdata/custom/world.js">World, Miller projection, medium resolution</a>'
        },

        mapNavigation: {
            enabled: true,
            buttonOptions: {
                verticalAlign: 'bottom'
            }
        },

        colorAxis: {
            min: 0
        },

        tooltip: {
            backgroundColor: 'none',
            borderWidth: 0,
            shadow: false,
            useHTML: true,
            padding: 0,
            pointFormat: '<span class="f32"><span class="flag {point.properties.hc-key}">' +
                '</span></span> {point.name}<br>' +
                '<span style="font-size:30px">{point.value}<sup style="font-size: 20px">$</sup></span>',
            positioner: function () {
                return {
                    x: 0,
                    y: 0
                };
            }
        },

        series: [{
            data: geoLocCurrentCost,
            name: 'Revenue Per Country',
            states: {
                hover: {
                    color: '#BADA55'
                }
            },
            dataLabels: {
                enabled: true,
                format: '{point.name}'
            }
        }]
    });

    /*
    """
     Function : Display the Countries wise Aggregated Current Cost 2018

    Returns:
        [type]: None
    """
    */

    var geoLocPreviousCost = $('div#geoLocPreviousCost').data('geolocpreviouscost');

    // Create the chart
    Highcharts.mapChart('geoLocPreviousCost', {
        chart: {
            map: 'custom/world'
        },

        title: {
            text: 'Per Country Revenue 2018'
        },

        subtitle: {
            text: 'Source map: <a href="http://code.highcharts.com/mapdata/custom/world.js">World, Miller projection, medium resolution</a>'
        },

        mapNavigation: {
            enabled: true,
            buttonOptions: {
                verticalAlign: 'bottom'
            }
        },

        colorAxis: {
            min: 0
        },

        tooltip: {
            backgroundColor: 'none',
            borderWidth: 0,
            shadow: false,
            useHTML: true,
            padding: 0,
            pointFormat: '<span class="f32"><span class="flag {point.properties.hc-key}">' +
                '</span></span> {point.name}<br>' +
                '<span style="font-size:30px">{point.value}<sup style="font-size: 20px">$</sup></span>',
            positioner: function () {
                return {
                    x: 0,
                    y: 0
                };
            }
        },

        series: [{
            data: geoLocPreviousCost,
            name: 'Revenue Per Country',
            states: {
                hover: {
                    color: '#BADA55'
                }
            },
            dataLabels: {
                enabled: true,
                format: '{point.name}'
            }
        }]
    });

    /*
  """
   Function : Sales w.r.t Under Writers 2018 vs 2019

    /*
  """
  */


  var listOfUW = $('div#getSalesByUnderWriterLastYear').data('listofuw');
  var salesByPreviousYear = $('div#getSalesByUnderWriterLastYear').data('salesbypreviousyear');
  var salesByCurrentYear = $('div#getSalesByUnderWriterLastYear').data('salesbycurrentyear');

  Highcharts.chart('getSalesByUnderWriterLastYear', {
    title: {
        text: 'Sales Per Underwriter 2018-2019'
    },
    xAxis: {
        categories: listOfUW
    },
    yAxis: [{
        min: 0,
        title: {
            text: 'Sale Price ($)'
        }
    }, {
        title: {
            text: ''
        },
        opposite: true
    }],
    legend: {
        align: 'left',
        verticalAlign: 'top',
        borderWidth: 0
    },
    tooltip: {
        shared: true
    },
    plotOptions: {
        column: {
            grouping: false,
            shadow: false,
            borderWidth: 0
        }
    },
    series: [{
        name: 'Underwriter Sales-2018',
        color: 'rgba(248,161,63,1)',
        data: salesByPreviousYear,
        tooltip: {
            valuePrefix: '$',
            valueSuffix: ''
        },
        pointPadding: 0.0,
        pointPlacement: 0.0,
        yAxis: 1
    }, {
        name: 'Underwriter Sales-2019',
        color: 'rgba(186,60,61,.9)',
        data: salesByCurrentYear,
        tooltip: {
            valuePrefix: '$',
            valueSuffix: ''
        },
        pointPadding: 0.25,
        pointPlacement: 0.0,
        yAxis: 1
    }
  ]

});

  /*
  """
   Function : HCC Sales w.r.t products 2018-2019

    /*
  """
  */

 var hccProductList = $('div#SalesByHCC').data('hccproductlist');
 var hccSalesPreviousYear = $('div#SalesByHCC').data('hccsalespreviousyear');
 var hccSalesCurrentYear = $('div#SalesByHCC').data('hccsalescurrentyear');
    Highcharts.chart('SalesByHCC', {

    chart: {
        type: 'line'
    },

    title: {
        text: 'HCC Sales Per Product 2018-2019'
    },

    yAxis: {
        allowDecimals: false,
        min: 0,
        title: {
            text: 'Sale Price ($)'
        }

    },
    xAxis: {
        tickWidth: 0,
        gridLineWidth: 1,
        categories: hccProductList,
    },
    legend: {
        align: 'left',
        verticalAlign: 'top',
        borderWidth: 0
    },
    tooltip: {
        shared: true,
        crosshairs: true
    },



    plotOptions: {
        series: {
            cursor: 'pointer',
            point: {
                events: {
                    click: function (e) {
                        hs.htmlExpand(null, {
                            pageOrigin: {
                                x: e.pageX || e.clientX,
                                y: e.pageY || e.clientY
                            },
                            headingText: this.series.name + '$',
                            maincontentText: this.x + ':<br/> ' +
                                this.y + ' sessions',
                            width: 200
                        });
                    }
                }
            },
            marker: {
                lineWidth: 1
            }
        }
    },
    series: [{
        name: 'Hcc Sales-2019',
        data: hccSalesCurrentYear,
        stack: '2019'
    },{
        name: 'Hcc Sales-2018',
        data: hccSalesPreviousYear,
        stack: '2018'
    }]
});

 /*
  """
   Function : Sales by Year 2018 and 2019

    /*
  """
  */


var previousYearSales = $('div#salesByYear').data('previousyearsales');
var currentYearSales = $('div#salesByYear').data('currentyearsales');
Highcharts.chart('salesByYear', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Sales Comparison 2018-2019'
    },
    xAxis: {
        categories: [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
    },
    yAxis: [{
        min: 0,
        title: {
            text: 'Sales Price ($)'
        }
    }, {
        min: 0,
        title: {
            text: 'Sales Price ($)'
        },
        opposite: true
    }],
    legend: {
        align: 'left',
        verticalAlign: 'top',
        borderWidth: 0,
        shadow: false
    },
    tooltip: {
        shared: true
    },
    plotOptions: {
        column: {
            grouping: false,
            shadow: false,
            borderWidth: 0
        }
    },
    series: [{
        name: 'Sales-2018',
        color: 'rgba(248,161,63,1)',
        data: previousYearSales,
        tooltip: {
            valuePrefix: '$',
            valueSuffix: ''
        },
        pointPadding: 0.0,
        pointPlacement: 0.0,
        yAxis: 1
    }, {
        name: 'Sales-2019',
        color: 'rgba(186,60,61,.9)',
        data: currentYearSales,
        tooltip: {
            valuePrefix: '$',
            valueSuffix: ''
        },
        pointPadding: 0.25,
        pointPlacement: 0.0,
        yAxis: 1
    }]
});

/*
  """
   Function : Sales by New and Old Customer 2018

    /*
  """
  */

 var newCustomerCountPreviousYear = $('div#newAndRepeatSalesCount').data('newcustomercountpreviousyear');
 var repeatCustomerCountPreviousYear = $('div#newAndRepeatSalesCount').data('repeatcustomercountpreviousyear');
 var newCustomerCountCurrentYear = $('div#newAndRepeatSalesCount').data('newcustomercountcurrentyear');
 var repeatCustomerCountCurrentYear = $('div#newAndRepeatSalesCount').data('repeatcustomercountcurrentyear');

 Highcharts.chart('newAndRepeatSalesCount', {
    chart: {
        type: 'column'
    },
    title: {
        text: ''
    },
    xAxis: {
        categories: [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December'
        ]
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Sales Price ($)'
        },
        stackLabels: {
            enabled: true,
            style: {
                fontWeight: 'bold',
                color: ( // theme
                    Highcharts.defaultOptions.title.style &&
                    Highcharts.defaultOptions.title.style.color
                ) || 'gray'
            }
        }
    },
    legend: {
        align: 'left',
        verticalAlign: 'top',
        borderWidth: 0,
        shadow: false
    },
    tooltip: {
        headerFormat: '<b>{point.x}</b><br/>',
        pointFormat: '{series.name}: {point.y}<br/>Total: {point.stackTotal}'
    },
    plotOptions: {
        column: {
            stacking: 'normal',
            dataLabels: {
                enabled: true
            }
        }
    },
    series: [{
        name: 'New Customers-2018',
        _colorIndex: 2,
        data: newCustomerCountPreviousYear,
        stack: '2018'
    }, {
        name: 'Repeat Customers-2018',
        _colorIndex: 0,
        data: repeatCustomerCountPreviousYear,
        stack: '2018'
    },
    {
        name: 'New Customers-2019',
        _colorIndex: 3,
        data: newCustomerCountCurrentYear,
        stack: '2019'
    }, {
        name: 'Repeat Customers-2019',
        _colorIndex: 1,
        data: repeatCustomerCountCurrentYear,
        stack: '2019'
    },

    ]
});







})