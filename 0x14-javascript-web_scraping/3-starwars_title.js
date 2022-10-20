#!/usr/bin/node
const request = require('request');
const url = 'http://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (error, _, body) {
  console.log(error || JSON.parse(body).title);
});
