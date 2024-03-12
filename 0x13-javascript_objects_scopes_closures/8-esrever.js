#!/usr/bin/node

exports.esrever = function (list) {
  // Initialize empty array to store reversed elements
  const reversed = [];

  // Iterate through input array in reverse and push each element into the 'reversed' array
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }

  // Return the array with reversed elements
  return reversed;
};
