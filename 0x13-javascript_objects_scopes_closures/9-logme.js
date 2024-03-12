#!/usr/bin/node

// This script defines a function 'logMe' and a global variable 'count' to log items with an incremental count.

// Global variable:
// - count: keeps track of the number of times 'logMe' is called

let count = 0;

// Function parameter:
// - item: the item to be logged

exports.logMe = function (item) {
  // Log the current count and the provided item using a template string
  console.log(`${count}: ${item}`);

  // Increment the count for the next call
  count++;
};
