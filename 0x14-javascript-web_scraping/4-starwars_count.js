#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else if (resp.statusCode !== 200) {
    console.log(`Status: ${resp.statusCode}`);
  } else {
    const charId = 'https://swapi-api.alx-tools.com/api/people/18/';
    const movies = JSON.parse(body).results;
    const count = movies.filter(movie => {
      for (const char of movie.characters) {
        if (char.includes(charId)) return true;
      }
      return false;
    });
    console.log(count.length);
  }
});
