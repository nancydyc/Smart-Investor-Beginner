"use strict";
console.log('result pages');
// Edit Watchlists:
// add star color should be prevented until server return message
// get the id of the event target and send to server
// server add it to database and return 200
// upon getting response 200, add color
$('.edit-watchlist').on('click', (evt) => {
    if (email === null) {
      alert('Please login to save stocks in your watchlist.');
    } else {
      let stock = evt.target.id;
      console.log(stock);
      let test = $(evt.target).hasClass('star3');
      if (test === true) {
          $(evt.target).removeClass('star3');
      } else {
      $(evt.target).addClass('star3');
      } // end if else changing star color
      editWatchlist(stock);
    } // end if else checking user login
}); // end click star

function editWatchlist(stockId) {
  console.log("0", stockId);
  let stockData = {'stock': stockId,
                   'email': email
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
  if (email === null) {
    console.log("no user login yet");
    evt.preventDefault();
    alert('Please login');    
  } else {
    console.log("Enjoy!");
  } 
}); //end click

// function showSavedStock () {
  $(document).ready( () => {

      //-if data-name is in the stock ids in watchlists 
    if (email !== null) {
      $.get('/watchlist', (res) => {
        for (const stock of res.watchlist) {
          console.log(stock.symbol);
          $(`#${stock.symbol}`).addClass('star3/'); 
        }; // end for
      }); // end get request     
    } else {
      console.log("Nothing happened");
    } // end if else check user login
  }); // end ready
// }; // end show saved stock

// user_watchlist = Watchlist.query.filter(Watchlist.user_id == 1).all()
// res.stock_id