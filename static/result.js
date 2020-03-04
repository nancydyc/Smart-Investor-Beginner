"use strict";
console.log('result pages');
// Edit Watchlists:
// add star color should be prevented until server return message
// get the id of the event target and send to server
// server add it to database and return 200
// upon getting response 200, add color
$('.edit-watchlist').on('click', (evt) => {
    const isSignedIn = gapi.auth2
      .getAuthInstance()
      .currentUser.get()
      .isSignedIn();

    if (!isSignedIn) {
      alert('Please login to save stocks in your watchlist.');
    } else {
      let stock = evt.target.id; // this is star icon id as well as stock id
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
  const stockData = {'stock': stockId,
                   'email': USEREMAIL
  }; 
  $.post('/watchlist', stockData, (res) => {
    console.log('2', stockData);
    console.log('3', res);
  }); // end post request
}; // end function editwatchlist


const USEREMAIL = localStorage.getItem("investorEmail");
console.log(USEREMAIL);

// alert user if they haven't login // Add if else condition
console.log('Below is for watchlist link');
$('.login').on('click', (evt) => {
  const isSignedIn = gapi.auth2
    .getAuthInstance()
    .currentUser.get()
    .isSignedIn();
  if (!isSignedIn) {
    console.log("no user login yet");
    evt.preventDefault();
    alert('Please login');    
  } else {
    console.log("Enjoy!");
  } 
}); //end click

