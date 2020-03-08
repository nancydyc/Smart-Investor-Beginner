"use strict";

function showSearchResult(evt) {
  evt.preventDefault();
    // TODO: get the fortune and show it in the #fortune-text div
  // let stockData = {'symbol': $('#search').value()};
  let stockData = $('#form').serialize();
  
  // Get matched stock symbols and company names
  $.get('/stock', stockData, (res) => {
    // const newSearch = $(
    //   '<ul id="new-search"></ul>'
    // );
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
            console.log(res)
            // const data = res.data.map((dailyInfo) => {
            //   return {x: dailyInfo.date, y: parseFloat(dailyInfo.ema)}
            // }); // end data

            // Create line chart
            Highcharts.chart('container', {
              data: {
                csv: res,
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
             
      }); // end click stockLink
      $('#search-results').append(stockLink);
      // $('#new-search').append(stockLink);
    }; // end for
    // $('#search-results').replaceWith(newSearch);
  }); // end get stock
}; // end function show search result

$('#form').on('submit', showSearchResult);

            