"use strict";

function showSearchResult(evt) {
  evt.preventDefault();
    // TODO: get the fortune and show it in the #fortune-text div
  // let stockData = {'symbol': $('#search').value()};
  let stockData = $('#form').serialize();
  // console.log(stockData);

  $.get('/stock', stockData, (res) => {
    $('#search-results').empty();
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

            