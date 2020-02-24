"use strict";

function showStockName(evt) {
  evt.preventDefault();
    // TODO: get the fortune and show it in the #fortune-text div
  // let stockData = {'symbol': $('#search').value()};
  let stockData = $('#form').serialize();
  // console.log(stockData);

  $.get('/stock', stockData, (res) => {
    // console.log(stockData);
    console.log(res);
    for (const stock of res.stocks) {
      console.log(stock);
      console.log(stock.symbol, stock.name);
      $('#names').append(`<li><a id="prices" data-click="${stock.symbol}" href="/stock/${stock.symbol}">${stock.symbol} ${stock.name}</li>`);
    };
    
  });
};

// function getRealTimePriceAndChart (evt) {
//   showRealtimePrice(evt)
//   displayChart(evt)
// }

$('#form').on('submit', showStockName);

$('#prices').on('click', displayPrice);

function displayPrice (evt) {

  evt.preventDefault();
  // let formData = {'symbol': $('#search').value()};
  let linkData = $('#prices').data();
  
  console.log(linkData);

  $.get('/stock/<symbol>', linkData, (res) => {
    console.log(res);
    $('#stock').html(res.symbol);
    $('#realtime').html(res.realtime);
  });

  
  $.get('/chart', linkData, (res) => {
    // console.log(res);
    // for (const daily of res) {
    // };
    // console.log(res.data);
    const data = res.data.map((dailyInfo) => {
      // console.log(dailyInfo);
      return {x: dailyInfo.date, y: dailyInfo.ema}
    });
    
    // console.log(data); 

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
};


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