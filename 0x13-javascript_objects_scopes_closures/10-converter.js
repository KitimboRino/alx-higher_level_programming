#!/usr/bin/node

// This script defines a function 'converter' that returns a nested function 'convert'. 
// The 'convert' function converts a given number to a string representation in the specified base.

// Function parameter:
// - base: the base to which numbers will be converted

exports.converter = function (base) {
  // Nested function:
  // - convert: takes a number as a parameter and converts it to a string representation in the specified base
  function convert(number) {
    return number.toString(base);
  }

  // Return the 'convert' function
  return convert;
};
