"use strict";
$(document).ready( () => {
  // let lineChart = $("#AAN");
  // lineChart.replaceWith('<canvas class="allmycharts" id="AAN"></canvas>');
  // replacing empty div with canvas works

  console.log('0.00');
  $.get('/linechart', (res) => {
    for (const stock of res.watchlist) {
      console.log(stock.symbol);
      // console.log(stock.datas);

      const chartData = stock.datas.map((dailyInfo) => {
        // console.log(dailyInfo);
        return {x: dailyInfo.date, y: dailyInfo.ema}
      });

      new Chart(
        $(`#${stock.symbol}`),
        {
          type: 'line',
          data: {
            datasets: [
              {
                label: 'Stock Monthly EMA Price',
                data: chartData
              }
            ]
          },
          options: {
            scales: {
              xAxes: [
                {
                  type: 'time',
                  distribution: 'series'
                }
              ]
            },
            tooltips: {
              callbacks: {

              }
            }
        }
      }); //end chart
    }; // end for 
  }); // end get
}); // end ready