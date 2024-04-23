#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else if (resp.statusCode !== 200) {
    console.log(`Status: ${resp.statusCode}`);
  } else {
    const antilles = 'https://swapi-api.alx-tools.com/api/people/18/';
    const movies = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < movies.length; i++) {
      if (movies[i].characters.includes(antilles)) count += 1;
    }
    console.log(count);
  }
});
