#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Initia;ise a counter to keep track of occurences
  let count = 0;

  // Iterate theought each element in the list
  list.forEach(element => {
    // Check current element equalt to the seachElement
    if (element === searchElement) {
      // If true, increment the counter
      count++;
    }
  });

  // Reteurn final count of occrences
  return count;
};
