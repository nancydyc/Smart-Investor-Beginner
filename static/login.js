"use strict";

function onSignIn(googleUser) {
  const profile = googleUser.getBasicProfile();
  // console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
  const userName = profile.getName();
  console.log(userName);
  // console.log('Image URL: ' + profile.getImageUrl());
  // console.log('Email: ' + profile.getEmail());
  const email = profile.getEmail();
  console.log(email);
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
};

$('#add-user-data').on('submit', (evt) => {
  evt.preventDefault();
  const userDetails = $('#user-detials').serialize();
  console.log(userDetails);
  $.post('/update', userDetails, (res) => {
    console.log(res);
  });
});



function signout() {
    const auth2 = gapi.auth2.init();
    // console.logs(isSignedIn.get());
    auth2.signOut().then(() => {
        alert("You've been successfully signed out.");
        $(".g-signin2").css("display", "block");
        $("#sign-out").css("display", "none");
        $("#pic").css("display", "none");
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
