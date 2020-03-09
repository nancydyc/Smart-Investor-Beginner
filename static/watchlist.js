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
      const cost = $(`#ave-cost-${stock}`).data('name');
      const shares = $(`#shares-${stock}`).data('name');
      console.log(cost, shares);
      $(`#total-${stock}`).text("100"); 
    }; // end for  
  }); // end get
}); //end click calculate