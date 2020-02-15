"use strict";

const displayChart () {
  // for (const price of ema) {
  //     priceList.push(price['EMA']);
  //     dateList.push()
  // }; //Why getting property works? Skipped getting index
  const formData = $('#search').serialize();
  console.log(formData);
  
  $.get('/chart', formData, (res) => {
    // const data = [];
    const data = res.data.map((dailyInfo) => {
      return {x: dailyInfo.date, y: dailyInfo.ema}
    }); 

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
    };
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

$('#search').on('submit', displayChart);


// data: {
//         labels: ['Oct', 'Nov', 'Dec', 'Jan', 'Feb'],
//         datasets: [{
//           label: 'Price',
//           data: $(priceList)
//         }]
//       }