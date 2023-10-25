#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (err, res, body) => {
  console.log('code:', res.statusCode);
});
