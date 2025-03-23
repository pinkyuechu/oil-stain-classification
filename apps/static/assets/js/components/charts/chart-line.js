'use strict';

// Sales chart
var SalesChart = (function() {
  // Variables
  var $chart = $('#chart-sales-dark');

  // Methods
  function init($chart) {
    var salesChart = new Chart($chart, {
      type: 'line',
      options: {
        scales: {
          yAxes: [{
            gridLines: {
              lineWidth: 1,
              color: Charts.colors.gray[900],
              zeroLineColor: Charts.colors.gray[900]
            },
            ticks: {
              callback: function(value) {
                if (!(value % 10)) {
                  return value + ' units'; // Changed from '$' to 'units'
                }
              }
            }
          }]
        },
        tooltips: {
          callbacks: {
            label: function(item, data) {
              var label = data.datasets[item.datasetIndex].label || '';
              var yLabel = item.yLabel;
              var content = '';

              if (data.datasets.length > 1) {
                content += '<span class="popover-body-label mr-auto">' + label + '</span>';
              }

              content += '<span class="popover-body-value">' + yLabel + ' units</span>'; // Changed from '$' to 'units'
              return content;
            }
          }
        }
      },
      data: {
        labels: ['Corn shoots', 'dadao cucumber', 'fulanxiaocai cucumber', 'xiaocaihenmang cucumber', 'xiaocaihenmang kelp', 'xiaofcaigongshe kelp'], // Changed to packaging types
        datasets: [{
          label: 'Packaging Types',
          data: [30, 45, 20, 60, 50, 40] // Example data
        }]
      }
    });

    // Save to jQuery object
    $chart.data('chart', salesChart);
  };

  // Events
  if ($chart.length) {
    init($chart);
  }
})();
