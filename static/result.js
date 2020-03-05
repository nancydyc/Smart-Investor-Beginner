"use strict";
$('.edit-watchlist').on('click', (evt) => {
  // use isSignedId to check if user's logged in >>> True/False
  const isSignedIn = gapi.auth2
    .getAuthInstance()
    .currentUser.get()
    .isSignedIn();

  if (!isSignedIn) {
    alert('Please login to save stocks in your watchlist.');
  } 
  //   else {
  //   let stock = evt.target.id; // this is star icon id as well as stock id
  //   console.log(stock);
  //   let test = $(evt.target).hasClass('star3');
  //   if (test === true) {
  //       $(evt.target).removeClass('star3');
  //   } else {
  //   $(evt.target).addClass('star3');
  //   } // end else changing star color
  //   editWatchlist(stock);
  // } // end else checking user login
}); // end click star

// alert user if they haven't login
$('.login-watchlist').on('click', (evt) => {
  const isSignedIn = gapi.auth2
    .getAuthInstance()
    .currentUser.get()
    .isSignedIn();
  if (!isSignedIn) {
    console.log("no user login yet");
    evt.preventDefault();
    alert('Please login');    
  } else {
    console.log("Let's go!");
  } 
}); //end click

