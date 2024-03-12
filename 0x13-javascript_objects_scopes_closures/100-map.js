#!/usr/bin/node

// Importing the list array from the file 100-data.js
const list = require('./100-data').list;

// Using the map function to create a new array
const mappedList = list.map(function (value, index) { return value * index; });

// Printing the initial list
console.log(list);

// Printing the new list
console.log(mappedList);
