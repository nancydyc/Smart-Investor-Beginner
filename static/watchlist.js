"use strict";
$(document).ready( () => {
  // Make line chart for each stock in the watchlist
  $.get('/linechart', (res) => {
    for (const stock of res.watchlist) {
      console.log(stock.symbol);

      // Create line chart
      const chartData = stock.datas.map((dailyInfo) => {
        return {x: dailyInfo.date, y: dailyInfo.ema}
      });

      new Chart(
        $(`#${stock.symbol}`),
        {
          type: 'line',
          data: {
            datasets: [
              {
                label: `${stock.symbol} Monthly EMA Price`,
                data: chartData
              }
            ]
          },
          options: {
            scales: {
              xAxes: [
                {
                  type: 'time',
                  distribution: 'series',
                  time: {
                    displayFormats: {
                      day: 'MM-DD-YYYY'
                    }
                  }
                }
              ]
            },
        }
      }); //end chart
    }; // end for 
  }); // end get
}); // end ready


//Calculate total holdings:

$('.calculate').on('click', (evt) => {
  $.get('/stocks', (res) =>{
    console.log(res.stocks);
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