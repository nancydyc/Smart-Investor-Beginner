"use strict";

$('#index-form').on('click', showSearchResultIndexPage);


function showSearchResultIndexPage(evt) {
  evt.preventDefault();

  let stockData = $('#index-form').serialize();
  // console.log(stockData);

  $.get('/stock', stockData, (res) => {
    $('#index-search-results').empty();
    for (const stock of res.stocks) {
      const stockLink = $(
        `
          <li data-symbol-name="${stock.symbol}">
            <a href="/${stock.symbol}">
              ${stock.symbol} ${stock.name}
            </a>
          </li>
        `
      );
      $('#index-search-results').append(stockLink);
    }; // end for
  }); // end get stock
}; // end function show search result

