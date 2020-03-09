"use strict";
$('.edit-watchlist').on('click', (evt) => {
  // use isSignedId to check if user's logged in >>> True/False
  const isSignedIn = gapi.auth2
    .getAuthInstance()
    .currentUser.get()
    .isSignedIn();

  if (!isSignedIn) {
    alert('Please login to save stocks in your watchlist.');
  } 
  //   else {
  //   let stock = evt.target.id; // this is star icon id as well as stock id
  //   console.log(stock);
  //   let test = $(evt.target).hasClass('star3');
  //   if (test === true) {
  //       $(evt.target).removeClass('star3');
  //   } else {
  //   $(evt.target).addClass('star3');
  //   } // end else changing star color
  //   editWatchlist(stock);
  // } // end else checking user login
}); // end click star

// alert user if they haven't login
$('.login-watchlist').on('click', (evt) => {
  const isSignedIn = gapi.auth2
    .getAuthInstance()
    .currentUser.get()
    .isSignedIn();
  if (!isSignedIn) {
    console.log("no user login yet");
    evt.preventDefault();
    alert('Please login');    
  } else {
    console.log("Let's go!");
  } 
}); //end click


// Click chart link to display this stock's chart
$('.chart').on('click', (evt) => {
  evt.preventDefault();
  let stock = evt.target.id;
  console.log(stock);
    // show line chart
  $.get(`/chart/${stock}`, (res) => {
    // console.log(res.weekly.data)
    const chartDataEMA = parseEMAData(res.ema.data);
    const chartDataWeekly = parseWeeklyData(res.weekly.data);
    // console.log(chartDataWeekly.timestamps);
    // Create line chart
    Highcharts.chart('container', {
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
      // plotOptions: {
      //   area: {
      //       fillColor: {
      //           linearGradient: {
      //               x1: 0,
      //               y1: 0,
      //               x2: 0,
      //               y2: 1
      //           },
      //           stops: [
      //               [0, Highcharts.getOptions().colors[0]],
      //               [1, Highcharts.color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
      //           ]
      //       },
      //       marker: {
      //           radius: 2
      //       }

      //   }
      // } // end plot options
    }); // end chart
  }); // end get data
}); //end click


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