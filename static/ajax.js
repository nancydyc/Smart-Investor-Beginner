"use strict";

function showSearchResult(evt) {
  evt.preventDefault();
    // TODO: get the fortune and show it in the #fortune-text div
  // let stockData = {'symbol': $('#search').value()};
  let stockData = $('#form').serialize();
  // console.log(stockData);

  $.get('/stock', stockData, (res) => {
    // console.log(stockData);
    // console.log(res);
    for (const stock of res.stocks) {
      // console.log(stock);
      // console.log(stock.symbol, stock.name);
      const stockLink = $(
        `
          <li data-symbol-name="${stock.symbol}">
            <a href="#">
              ${stock.symbol} ${stock.name}
            </a>
          </li>
        `
      );

      stockLink.on('click', (evt) => {
        evt.stopPropagation(); // prevent parent event handlers from being executed
        // const clickedLink = ;
        // const stockSymbol = $(evt.target).data('stockSymbol');

        // show stock symbol and price
        $.get(`/stock/${stock.symbol}`, (res) => {
          // console.log(res);
          $('#stock').html(res.symbol);
          $('#realtime').html(res.realtime);
        });
        // show line chart
          $.get(`/chart/${stock.symbol}`, (res) => {
            console.log(res);
            const data = res.data.map((dailyInfo) => {
              // console.log(dailyInfo);
              return {x: dailyInfo.date, y: dailyInfo.ema}
            });
            
            console.log(data); 

            new Chart(
              $('#price-chart'),
              {
                type: 'line',
                data: {
                  datasets: [
                    {
                      label: 'Stock Monthly EMA Price',
                      data: data
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
                  }
              }
            });
          });

      });

      $('#search-results').append(stockLink);
    };
    
  });
};

// function getRealTimePriceAndChart (evt) {
//   showRealtimePrice(evt)
//   displayChart(evt)
// }

$('#form').on('submit', showSearchResult);


// $('#prices').on('click', displayChart);

// function displayChart (evt) {
  

// };


// data: {
//         labels: ['Oct', 'Nov', 'Dec', 'Jan', 'Feb'],
//         datasets: [{
//           label: 'Price',
//           data: $(priceList)
//         }]
//       }

      // options: {
      //   title:{
      //     display: true,
      //     text: 'Stock Monthly EMA Price',
      //     position: 'rignt'
      //   },
      // } // Once I add options, the chart is gone.
//     }
//   );
// };