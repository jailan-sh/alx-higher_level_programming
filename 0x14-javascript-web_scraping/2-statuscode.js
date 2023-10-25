#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request.get(url, (err, res, body) => {
  if (err) {

  } else {
    console.log('code: ', res.statusCode);
  }
});
