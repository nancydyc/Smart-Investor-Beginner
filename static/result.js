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

const email = localStorage.getItem("investorEmail");
console.log(email);

// alert user if they haven't login // Add if else condition
console.log('0');
$('.login').on('click', (evt) => {
  console.log('alert about to start');
  if (email === null) { // not working ? how to solve?
    console.log("no user login yet");
    evt.preventDefault();
    alert('Please login');    
  } else {
    console.log("Enjoy!");
  } 
}); //end click

// function showSavedStock () {
//   $(document).ready( () => {
//     $.get('/savedstock'), (res) {
//       -if data-name is in the stock ids in watchlists 
//       -$(data-name).addClass('star3');
//     }

//   } 
// }

// user_watchlist = Watchlist.query.filter(Watchlist.user_id == 1).all()
// res.stock_id