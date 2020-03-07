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
            // console.log(res.symbol, res.data);
            // const data = res.data.map((dailyInfo) => {
            //   // console.log(dailyInfo);
            //   return {x: dailyInfo.date, y: parseFloat(dailyInfo.ema)}
            // }); // end data
            console.log(res.symbol);
            console.log(res.data.ema);

            // newLineChart
            // Create the chart
            // Highcharts.stockChart('container', {
            //   rangeSelector: {
            //     selected: 1
            //   },
            //   series: [{
            //     name: `${res.symbol} EMA Price`,
            //     data: [{x: "2020-03-06", y: 267.5853}, {x: "2020-02-28", y: 266.5719}, {x: "2020-02-21", y: 264.4554}],  // predefined JavaScript array
            //     tooltip: {
            //     valueDecimals: 2
            //     }  
            //   }]
            // });
            Highcharts.chart('container', {
                chart: {
                    type: 'line'
                },
                title: {
                    text: `${res.symbol} EMA Price`
                },
                xAxis: {
                    type: 'datetime' 
                },
                yAxis: {
                    title: {
                        text: 'Fruit eaten'
                    }
                },
                series: [{
                    name: `${res.symbol}`,
                    data: res.data.ema
                }],
                tooltip: {
                  crosshairs: [true]
                }
            });
  
            



            // Highcharts.stockChart('container', {

            //   title: {
            //       text: 'AAPL Stock Price'
            //   },

            //   // subtitle: {
            //   //     text: 'Demo of placing the range selector above the navigator'
            //   // },

            //   rangeSelector: {
            //       floating: true,
            //       y: -65,
            //       verticalAlign: 'bottom'
            //   },

            //   navigator: {
            //       margin: 60
            //   },

            //   series: [{
            //       name: 'AAPL',
            //       data: data,
            //       tooltip: {
            //           valueDecimals: 2
            //       }
            //   }]
            // });



          }); // end get

      }); // end click stockLink

      $('#search-results').append(stockLink);
    }; // end for
    
  }); // end get stock
}; // end function show search result

$('#form').on('submit', showSearchResult);


// new Chart(
//   $('#price-chart'),
//   {
//     type: 'line',
//     data: {
//       // labels: res.dates,
//       datasets: [
//         {
//           label: 'Stock Monthly EMA Price',
//           data: data
//         }
//       ]
//     },
//     options: {
//       scales: {
//         xAxes: [
//           {
//             type: 'time',
//             distribution: 'series',
//             time: {
//               // unit : "day",
//               displayFormats: {
//                 day: 'MM-DD-YYYY'
//               }
//             }
//           }
//         ]
//       }
//   }
// });