$(function () {
  var timestamp = $('#salesOverview').data('timestamp');
  var currCost = $('#salesOverview').attr('data-currCost');
  var options = {
    animations: {
      enabled: true,
      easing: 'easeinout',
      speed: 800,
      animateGradually: {
        enabled: true,
        delay: 150
      },
      dynamicAnimation: {
        enabled: true,
        speed: 350
      }
    },
    subtitle: {
      text: 'Sale\'s Time Series',
      align: 'center',
      margin: 10,
      offsetX: 0,
      offsetY: 0,
      floating: true,
      style: {
        fontSize:  '20px',
        color:  '#000'
      },
  },

    toolbar: {
      show: true,
      tools: {
        download: true,
        selection: true,
        zoom: true,
        zoomin: true,
        zoomout: true,
        pan: true,
        reset: true | '<img src="/static/icons/reset.png" width="20">',
        customIcons: []
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'smooth'
    },
    chart: {
      height: 350,
      type: 'area',
      background: '#fff',
      zoom: {
        enabled: true
      },
    },
    series: [{
      name: 'sales',
      data: eval(currCost)
    }],
    xaxis: {
      type: 'datetime',
      categories: eval(timestamp),
      labels: {
        datetimeFormatter: {
          year: 'yyyy',
          month: 'MMM',
          day: 'dd MMM',
          hour: 'HH:mm'
        },
        offsetX: 0,
        offsetY: 0,
      },
      title: {
        text: 'Time in Days',
        offsetX: 0,
        offsetY: 0,
        position: 'left',
        style: {
            color: undefined,
            fontSize: '12px',
            fontFamily: 'Helvetica, Arial, sans-serif',
            cssClass: 'apexcharts-xaxis-title',
        },
      },
    },
    yaxis: {
      type: 'datetime',
      categories: eval(currCost),
      labels: {
        formatter: function (value) {
          return value + " $";
        },
        offsetX: 0,
        offsetY: 0,
      },
      tickAmount: 8,
    },
    legend: {
      position: 'top',
      show: true
    },
    title: {
      text: 'Sales ($)',
      style: {
          color: undefined,
          fontSize: '12px',
          fontFamily: 'Helvetica, Arial, sans-serif',
          cssClass: 'apexcharts-xaxis-title',
          fontWeight : 'bold'
      },
    },
  }

  var chart = new ApexCharts(document.querySelector("#salesOverview"), options);
  chart.render();


  /*
  """
   Function : Display the Countries wise Aggregated Current Cost

  Returns:
      [type]: None
  """
  */

  var geoCountriesCount = $('div#geoCountriesCount').data('geocountriescount');

  // Create the chart
  Highcharts.mapChart('geoCountriesCount', {
    chart: {
      map: 'custom/world'
    },

    title: {
      text: 'G1G Customers Around the World'
    },

    subtitle: {
      text: 'G1G valued customers'
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
        '<span style="font-size:20px">Number of Visitors =</span>  <span style="font-size:30px">{point.value}</span>',
      positioner: function () {
        return {
          x: 0,
          y: 0
        };
      }
    },

    series: [{
      data: geoCountriesCount,
      name: 'Number of Customers Per Country',
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
   Function : Sales w.r.t Under Writers

  Returns:
      [type]: None
  """
  */

  var salesUnderwriter = $('div#SalesByUnderwriter').data('salesunderwriter');
  Highcharts.chart('SalesByUnderwriter', {
    chart: {
      type: 'pie',
      options3d: {
        enabled: true,
        alpha: 45
      }
    },
    title: {
      text: 'Total Sales w.r.t. Underwriters'
    },
    accessibility: {
      point: {
        valueSuffix: '%'
      }
    },
    subtitle: {
      text: 'Cumulated Sales in $'
    },
    plotOptions: {
      pie: {
        innerSize: 100,
        depth: 45
      }
    },
    series: [{
      name: 'Received amount',
      data: salesUnderwriter,
    }]
  });





})

$(function () {
  /* BOOTSTRAP SLIDER */
  $('.slider').bootstrapSlider();
})