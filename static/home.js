"use strict";

function showSearchResult(evt) {
  evt.preventDefault();
    // TODO: get the fortune and show it in the #fortune-text div
  // let stockData = {'symbol': $('#search').value()};
  let stockData = $('#form').serialize();
  // console.log(stockData);

  $.get('/stock', stockData, (res) => {
    
    for (const stock of res.stocks) {
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

        // show stock symbol and price
        $.get(`/stock/${stock.symbol}`, (res) => {

          $('#stock').html(res.symbol);
          $('#realtime').html(res.realtime);

        });
          // show line chart
          $.get(`/chart/${stock.symbol}`, (res) => {

            const data = res.data.map((dailyInfo) => {

              return {x: dailyInfo.date, y: parseFloat(dailyInfo.ema)}
            
            }); // end data

            // Create line chart
            new Chart(
              $('#price-chart'),
              {
                type: 'line',
                data: {
                  // labels: res.dates,
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
                        distribution: 'series',
                        time: {
                          // unit : "day",
                          displayFormats: {
                            day: 'MM-DD-YYYY'
                          }
                        }
                      }
                    ]
                  }
                }
            });// end line chart 
          }); // end get
      }); // end click stockLink
      $('#search-results').append(stockLink);
    }; // end for
  }); // end get stock
}; // end function show search result

$('#form').on('submit', showSearchResult);


$(document).ready( () => {
  $.get('https://www.alphavantage.co/query?function=EMA&symbol=LK&interval=weekly&time_period=10&series_type=open&datatype=csv&apikey=G91S3ATZL5YIK83E', (data) => {
    console.log(data);
    Highcharts.chart('container', {
                  data: {
                    csv: data,
                  },
                  chart: {
                      type: 'area',
                      zoomType: 'x'
                  },
                  title: {
                      text: 'Stock EMA Price'
                  },
                  // xAxis: {
                  //     type: 'datetime'
                  // },
                  yAxis: {
                      title: {
                          text: 'Stock Price'
                      }
                  },
                  // series: [{
                  //     // name: `${res.symbol}`,
                  //     name: '30 Days EMA'
                  // }],
                  tooltip: {
                    crosshairs: [true, true]
                  }
              });
  }); // end get data
}); // end ready
            // console.log(res.symbol);
            // console.log(res.data);

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
            