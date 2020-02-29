"use strict";

function onSignIn(googleUser) {
  const profile = googleUser.getBasicProfile();
  // console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
  // console.log('Name: ' + profile.getName());
  // console.log('Image URL: ' + profile.getImageUrl());
  // console.log('Email: ' + profile.getEmail());
  email = profile.getEmail();
  console.log(email);
  userData = {'email': email,
              'buying_power': $('#user-details').val();
  };
  $.post('/adduser', userData, (res) => {
    console.log('New user added.')
  }); 
  $(".g-signin2").css("display", "none");
  $(".data").css("display", "block");
  $("#pic").attr('src', profile.getImageUrl());
  $("#pic-big").attr('src', profile.getImageUrl());
  $("#email").text(profile.getEmail());
};

function signout() {
    const auth2 = gapi.auth2.init();
    // console.logs(isSignedIn.get());
    auth2.signOut().then(() => {
        alert("You've been successfully signed out.");
        $(".g-signin2").css("display", "block");
    }); //end auth2.signOut
}; // end signout function


// // Send email and buying power to database after sign-in

// function sendUserDetails(stockId) {
//   console.log("0", stockId);
//   let stockData = {'stock': stockId,
//                    'user': 1
//   }; // stockData
//   $.post('/watchlist', stockData, (res) => {
//     console.log('2', stockData);
//     console.log('3', res);
//   }); // end post request
// }; // end function editwatchlist
