"use strict";   

function onSignIn(googleUser) {
  const profile = googleUser.getBasicProfile();

  // Send email to server to see if this is a new user
  const email = profile.getEmail();

  localStorage.setItem("investorEmail", email);

  const userData = {'email': email};
  console.log(userData);
  $.post('/login', userData, (res) => {
    console.log(res);
  });

  // Hide sign-in button
  // Display profile picture and show email on profile page
  $(".g-signin2").css("display", "none");
  $("#user-menu").css("display", "block");
  // $(".g-data").css("display", "block");
  $("#pic").attr('src', profile.getImageUrl());
  $("#pic-big").attr('src', profile.getImageUrl());
  $("#email").text(profile.getEmail());

  // Mark stars blue for Saved Stocks after user login
  // Get stock ids from database watchlists table 
  $.get('/saved', (res) => {
    for (const savedStockId of res.watchlist) {
      $(`#${savedStockId[0]}`).addClass('star3'); 
    }; // end for
  }); // end get request
  clickStarButton (email);
  deleteFromWatchlist(email);
}// end Sign-in function


// Click the star to edit Watchlists:
// Prevent this feature until the user is signed in
function clickStarButton (email) {
  $('.edit-watchlist').on('click', (evt) => {
    // use isSignedId to check if user's logged in >>> True/False
    const isSignedIn = gapi.auth2
      .getAuthInstance()
      .currentUser.get()
      .isSignedIn();
    if (!isSignedIn) {
      alert('Please login to save stocks in your watchlist.');
    } else {
      const isSignedIn = gapi.auth2
        .getAuthInstance()
        .currentUser.get()
        .isSignedIn();
      // below is star icon id as well as stock id
      let stock = evt.target.id; 
      console.log(stock);
      let starColor = $(evt.target).hasClass('star3');
      if (starColor === true) {
          $(evt.target).removeClass('star3');
      } else {
      $(evt.target).addClass('star3');
      } // end else changing star color
      console.log(email);
      editWatchlist(stock, email);
    }
  }); // end click star
} // end function clickstarbtn


// Click delete button in watchlist page to edit watchlists
function deleteFromWatchlist(email) {
  $('.delete').on('click', (evt) => {
  let stock = $(evt.target).data('name');
  console.log(stock);
  editWatchlist(stock, email);
  console.log('Deleted', stock);
  $(`#watch-${stock}`).hide();
  }); // end click delete btn
} // end function delete


// Send data to server for functionality
function editWatchlist(stock, email) {
  const stockData = {'stock': stock,
                   'email': email
  }; 
  $.post('/watchlist', stockData, (res) => {
    console.log('Editing result: ', res);
  }); // end post request
} // end function editwatchlist


function signOut() {
    const auth2 = gapi.auth2.init();
    
    auth2.signOut().then(() => {
        alert("You've been successfully signed out.");
        $(".g-signin2").css("display", "block");
        $("#user-menu").css("display", "none");
        $("#pic").css("display", "none");
        localStorage.removeItem("investorEmail");
        $('.edit-watchlist i').removeClass('star3'); 
        //back to homepage after sign out
    }); //end auth2.signOut
} // end signout function


// Profile page:
// Send email and buying power to database after sign-in
$('#user-details').on('submit', (evt) => {
  evt.preventDefault();
  const userDetails = $('#user-details').serialize();
  console.log(userDetails);
  $.post('/update', userDetails, (res) => {
    // console.log(userDetails);
    console.log(res);
  }); // end post
}); // end submit


//Before sign in
// alert user if they haven't login
$('.login-required').on('click', (evt) => {
  const isSignedIn = gapi.auth2
    .getAuthInstance()
    .currentUser.get()
    .isSignedIn();
  if (!isSignedIn) {
    console.log("no user login yet");
    evt.preventDefault();
    alert('Please login to use watchlist');    
  } else {
    console.log("Let's go!");
  } 
}); //end click