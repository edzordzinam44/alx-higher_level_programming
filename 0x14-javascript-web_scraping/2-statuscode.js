#!/usr/bin/node

const request = require('request');
const pathUrl = process.argv[2];

request(pathUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(response.statusCode);
  }
});
