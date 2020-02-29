"use strict";
console.log('result pages');

$('.edit-watchlist').on('click', (evt) => {
    let stock = evt.target.id;
    console.log(stock);
    let test = $(evt.target).hasClass('star3');
    if (test === true) {
        $(evt.target).removeClass('star3');
    } else {
    $(evt.target).addClass('star3');
    }
    editWatchlist(stock);
});
// add star color should be prevented until server return message
// get the id of the event target and send to server
// server add it to database and return 200
// upon getting response 200, add color
// console.log('0.00');
function editWatchlist(stockId) {
  console.log("0", stockId);
  let stockData = {'stock': stockId,
                   'user': 1
  }; // stockData
  $.post('/watchlist', stockData, (res) => {
    console.log('2', stockData);
    console.log('3', res);
  }); // end post request
}; // end function editwatchlist


// alert user if they haven't login
console.log('0');
$('.login').on('click', (evt) => {
  console.log('alert about to start');
  evt.preventDefault();
  alert('Please login');
}); //end click
