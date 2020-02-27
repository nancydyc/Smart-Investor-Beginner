"use strict";

const star = $(
  `
    <th id="${data.stock_id}" data-symbol-name="${data.stock_id}">
      <i class="far fa-star"></i>
    </th>
  `
  );

// const yellowstar = $(
//   `
//     <th class="star2" data-symbol-name="${data.stock_id}">
//       <i class="far fa-star"></i>
//     </th>
//   `
//   );
star.on('click', (evt) => {
  $('#${data.stock_id}').addClass('star2');
});


// send the symbol to server and change database

// star.on('click', (evt) => {
//   evt.preventDefault(); 
//   $.post(`/watchlist/${data.stock_id}`, (res) => {
    
//   };