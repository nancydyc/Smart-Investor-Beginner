"use strict";

function showSearchResult(evt) {
  evt.preventDefault();
    // TODO: get the fortune and show it in the #fortune-text div
  // let stockData = {'symbol': $('#search').value()};
  let stockData = $('#form').serialize();
  
  // Get matched stock symbols and company names
  $.get('/stock', stockData, (res) => {

    // $('#search-results').empty();
    
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
        $('#search-results').empty();

        evt.stopPropagation(); // prevent parent event handlers from being executed

        // show stock symbol and price
        $.get(`/stock/${stock.symbol}`, (res) => {

          $('#stock-realtime').css("display", "block");
          $('#stock').html(res.symbol);
          let realtime = parseFloat(res.realtime).toFixed(2);
          console.log(realtime);
          $('#realtime').html(realtime);
        });
          // show line chart
          $.get(`/chart/${stock.symbol}`, (res) => {
            // console.log(res.weekly.data)
            const chartDataEMA = parseEMAData(res.ema.data);
            const chartDataWeekly = parseWeeklyData(res.weekly.data);
            // console.log(chartDataWeekly.timestamps);
            // Create line chart
            Highcharts.chart('container', {
              // data: {
              //   csv: res,
              // },

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
             
      }); // end click stockLink
      $('#search-results').append(stockLink);
      // $('#new-search').append(stockLink);
    }; // end for
    // $('#search-results').replaceWith(newSearch);
  }); // end get stock
}; // end function show search result

$('#form').on('submit', showSearchResult);

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