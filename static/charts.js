"use strict";

function showRealtimePrice(evt) {
  evt.preventDefault();
    // TODO: get the fortune and show it in the #fortune-text div
  // let stockData = {'symbol': $('#search').value()};
  let stockData = $('#form').serialize();
  // console.log(stockData);

  $.get('/stock', stockData, (res) => {
    // console.log(stockData);
    // console.log(res);
    $('#stock').html(res.symbol);
    $('#realtime').html(res.realtime);
  });

};

$('#form').on('submit', showRealtimePrice);


function displayChart (evt) {
  // for (const price of ema) {
  //     priceList.push(price['EMA']);
  //     dateList.push()
  // }; //Why getting property works? Skipped getting index
  evt.preventDefault();
  
  // let formData = {'symbol': $('#search').value()};
  let formData = $('#form').serialize();
  
  // console.log(formData);
  
  $.get('/chart', formData, (res) => {

    for (const daily in res) {
      

    }

    const data = res.data.map((dailyInfo) => {
      return {x: dailyInfo.date, y: dailyInfo.ema}
    });
    }
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
        }
      }
    );
  });
};  

$('#chart').on('click', displayChart);


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