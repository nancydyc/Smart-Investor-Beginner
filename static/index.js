"use strict";

$('#chart-btn').on('click', (evt) => {
  console.log('inside submit');
  let symbol = $("#chart-btn").data("name");
  console.log(symbol);
  // show line chart          
  $.get(`/chart/${symbol}`, (res) => {
    
    const chartDataEMA = parseEMAData(res.ema.data);
    const chartDataWeekly = parseWeeklyData(res.weekly.data);
    console.log(chartDataWeekly.data)
    // Create line chart
    Highcharts.chart('index-container', {

      chart: {
          type: 'line',
          zoomType: 'x'
      },
      title: {
          text: `${res.ema.stock} Stock Price Line Chart`
      },
      xAxis: {
          categories: chartDataWeekly.timestamps
      },
      yAxis: {
          title: {
              text: 'Stock Price'
          }
      },
      series: [
        {
          name: `${res.ema.stock} 10 Days EMA`,
          data: chartDataEMA.data,
          turboThreshold: 2000 // set a value to accept large data size
        },
      
        {
          name: `${res.weekly.stock} Weekly Open Price`,
          data: chartDataWeekly.data,
          turboThreshold: 2000 // set a value to accept large data size
        }
      ],
      legend: {
        align: 'left',
        verticalAlign: 'top',
        borderWidth: 0
      },
      tooltip: {
        shared: true,
        crosshairs: [true, true],
        valueDecimals: 2
      }
      
    }); // end chart
  }); // end get data
}); // end click show chart button


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


function parseWeeklyData (res) {
  const data = [];
  const timestamps = [];
  const lines = res.split("\n");
  
  $.each(lines, function (lineNumber, line) {
    
    if (lineNumber !== 0) {
      const fields = line.split(",");
      if (fields.length === 6) {
        const timestamp = fields[0];
        const value = parseFloat(fields[1]);
        data.push([timestamp, value]);
        timestamps.push(timestamp);
      } 
    } // end if
  }); // end each
  timestamps.reverse();
  // console.log(timestamps.slice(9));
  data.reverse();
  return {'timestamps': timestamps.slice(9), 'data': data.slice(9)};
}        