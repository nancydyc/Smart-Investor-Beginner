"use strict";

let priceList = []
let dateList = []
// const daily_ema = [('2020-02-13', {'EMA': '37.6700'}),
//  ('2020-02-12', {'EMA': '37.6521'}),
//  ('2020-02-11', {'EMA': '37.5909'}),
//  ('2020-02-10', {'EMA': '37.5675'}),
//  ('2020-02-07', {'EMA': '37.7983'})];

for (const price of daily_ema) {
    priceList.push(price['EMA']);
}; //Why getting property works? Skipped getting index

let priceChart = new Chart(
  $('#price-chart'),
  {
    type: 'line',
    data: {
      labels: ['Oct', 'Nov', 'Dec', 'Jan', 'Feb'],
      datasets: [{
        label: 'Price',
        data: $(priceList)
      }],
/*      options: {
      title:{
        display: true,
        text: 'Stock Monthly Average Price',
    //     fontSize: 25
      },
      legend: {
        position: 'rignt'*/
      // }
    }
  }
);
