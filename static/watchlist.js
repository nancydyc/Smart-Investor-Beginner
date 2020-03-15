"use strict";
$(document).ready( () => {
  // Make line chart for each stock in the watchlist
  $.get('/linechart', (res) => {
    for (const stock of res.watchlist) {
      console.log(stock.symbol);

      // Create line chart
      const chartDataEMA = parseEMAData(stock.datas.data);
      // console.log(chartDataEMA.timestamps);

      Highcharts.chart(`${stock.symbol}`, {
        chart: {
            type: 'area',
            zoomType: 'x'
        },
        title: {
            text: `${stock.symbol} Stock Price Line Chart`
        },
        xAxis: {
            categories: chartDataEMA.timestamps
        },
        yAxis: {
            title: {
                text: 'Stock Price'
            }
        },
        series: [
          {
            name: `${stock.symbol} 10 Days EMA`,
            data: chartDataEMA.data,
            turboThreshold: 2000 // set a value to accept large data size
          }
        ],
        legend: {
          align: 'left',
          verticalAlign: 'top',
          borderWidth: 0
        },
        tooltip: {
          crosshairs: [true, true],
          valueDecimals: 2
        },
        plotOptions: {
        area: {
            fillColor: {
                linearGradient: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 1
                },
                stops: [
                    [0, Highcharts.getOptions().colors[0]],
                    [1, Highcharts.color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
                ]
            },
            marker: {
                radius: 2
            }

        }
      } // end plot options 
      }); // end chart
    }; // end for 
  }); // end get
}); // end ready


//Calculate total holdings:
$('#calculate').on('click', (evt) => {
  evt.preventDefault();
  // evt.stopPropagation();
  
  $.get('/stocks', (res) =>{
    
    for (const stock of res.stocks) {
      console.log(stock);
      const data = $(`#form-${stock}`).serialize();
      $.get('/holdings', data, (res) => {
        console.log(res);
        
        $(`#total-${stock}`).text(res.data); 
      }); // end get holdings
    }; // end for  
  }); // end get stocks
}); //end click calculate


// Process data from server before being used in Highchart
function parseEMAData (res) {
  const data = [];
  const timestamps = [];
  const lines = res.split("\n");
  $.each(lines, function (lineNumber, line) {
    if (lineNumber !== 0) {
      const fields = line.split(",");
      if (fields.length === 2) {
        const timestamp = fields[0];
        const value = parseFloat(fields[1]);
        data.push([timestamp, value]);
        timestamps.push(timestamp);
      } 
    } // end if
  }); // end each
  return {'timestamps': timestamps.reverse(), 'data': data.reverse()};
}