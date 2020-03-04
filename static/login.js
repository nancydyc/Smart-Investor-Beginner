"use strict";   

function onSignIn(googleUser) {
  const profile = googleUser.getBasicProfile();
  // console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
  const userName = profile.getName();
  // console.log(userName);
  // console.log('Image URL: ' + profile.getImageUrl());
  // console.log('Email: ' + profile.getEmail());
  const email = profile.getEmail();
  // console.log(email);
  localStorage.setItem("investorEmail", email);
  const userData = {'email': email,
                    'name': userName
  };
  console.log(userData);
  $.post('/login', userData, (res) => {
    console.log(res);
  }); 
  $(".g-signin2").css("display", "none");
  $(".data").css("display", "block");
  $("#pic").attr('src', profile.getImageUrl());
  $("#pic-big").attr('src', profile.getImageUrl());
  $("#email").text(profile.getEmail());
    // Mark stars blue for Saved Stocks after user login
  // Get stock ids from database watchlists table 
  $.get('/saved', (res) => {
    for (const saved of res.watchlist) {
      // console.log(saved[0]); this is stock id
      $(`#${saved[0]}`).addClass('star3'); 
    }; // end for
  }); // end get request     
};


function signOut() {
    const auth2 = gapi.auth2.init();
    // console.logs(isSignedIn.get());
    auth2.signOut().then(() => {
        alert("You've been successfully signed out.");
        $(".g-signin2").css("display", "block");
        $("#sign-out").css("display", "none");
        $("#pic").css("display", "none");
        localStorage.removeItem("investorEmail");
        $('.edit-watchlist i').removeClass('star3');
    }); //end auth2.signOut
}; // end signout function


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