"use strict";

let priceList = []
let dateList = []
// const daily_ema = [('2020-02-13', {'EMA': '37.6700'}),
//  ('2020-02-12', {'EMA': '37.6521'}),
//  ('2020-02-11', {'EMA': '37.5909'}),
//  ('2020-02-10', {'EMA': '37.5675'}),
//  ('2020-02-07', {'EMA': '37.7983'})];
// You can get keys use object.keys()

// for (const price of daily_ema) {
//     priceList.push(price['EMA']);
// }; //Why getting property works? Skipped getting index

const formData = $('#search').value();
$.get('/stock', formData, (res) => {
  const data = [];
  for (const daily of res {
    data.push({x: date, y: dailyPrice.})
  }

});

const priceChart = new Chart(
  $('#price-chart'),
  {
    type: 'line',
    data: {
      labels: ['Oct', 'Nov', 'Dec', 'Jan', 'Feb'],
      datasets: [{
        label: 'Price',
        data: $(priceList)
      }]
    }
    // options: {
    //   title:{
    //     display: true,
    //     text: 'Stock Monthly EMA Price',
    //     position: 'rignt'
    //   },
    // } // Once I add options, the chart is gone.
  }
);
