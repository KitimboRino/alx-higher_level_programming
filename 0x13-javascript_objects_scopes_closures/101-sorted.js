#!/usr/bin/node

// Importing the dict dictionary from the file 101-data.js
const list = require('./101-data').dict;

// Creating a new dictionary where keys are occurrences and values are lists of user ids
const sorted = {};

// Iterate through the keys of the original dictionary
Object.keys(list).forEach(key => {
  // Use the logical OR to initialize the list if it doesn't exist yet
  sorted[list[key]] = sorted[list[key]] || [];

  // Push the current user id to the list corresponding to the occurrences value
  sorted[list[key]].push(key);
});

// Printing the new dictionary
console.log(sorted);
