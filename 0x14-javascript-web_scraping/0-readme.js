#!/usr/bin/node
const { ok } = require('assert');
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  console.log(err || data);
});
ok
