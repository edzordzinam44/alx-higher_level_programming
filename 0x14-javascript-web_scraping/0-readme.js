#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    // Handle the error
    console.error((err));
  } else {
    // Print the file content
    console.log(data);
  }
});
