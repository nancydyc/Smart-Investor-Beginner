"use strict";
console.log('0');
// const stockSymbol = $(evt.target).data();
const stockSymbol = "AAP";
// console.log('1', stockSymbol);

$.post('/watchlist/stockSymbol', stockSymbol, (res) => {
  console.log('2', stockSymbol);
  console.log('3', res);
  evt.preventDefault();
  // evt.stopPropagation();
  // const star = $(
  // `
  //   <th id=`watch-${stockSymbol}` data-symbol-name=`${stockSymbol}`>
  //     <i id=`star-${stockSymbol}` class="far fa-star"></i>
  //   </th>
  // `
  // );

  $('#star-AAP').on('click', () => {
    $('#star-AAP').addClass('star2');
  });
};

// send the symbol to server and change database

// star.on('click', (evt) => {
//   evt.preventDefault(); 
//   $.post(`/watchlist/${data.stock_id}`, (res) => {
    
//   };