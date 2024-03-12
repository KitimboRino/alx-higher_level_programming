#!/usr/bin/node

// Import the 'fs' (file system) module for file operations
const fs = require('fs');

// Extract file paths from command line arguments
const src1 = process.argv[2];
const src2 = process.argv[3];
const dest = process.argv[4];

// Function to handle the callback for reading and appending files
function appendToFile (err, data) {
  if (err) {
    // Log an error message if there's an issue reading the file
    return console.error(err);
  }

  // Append the file content to the destination file
  fs.appendFile(dest, data, function (err) {
    if (err) {
      // Log an error message if there's an issue appending to the destination file
      console.error(err);
    }
  });
}

// Read the content of the first file and append it to the destination file
fs.readFile(src1, 'utf8', (err, data) => {
  appendToFile(err, data);

  // Read the content of the second file and append it to the destination file
  fs.readFile(src2, 'utf8', appendToFile);
});
