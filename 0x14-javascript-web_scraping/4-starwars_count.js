#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else if (resp.statusCode !== 200) {
    console.log(`Status: ${resp.statusCode}`);
  } else {
    const charId = 18;
    const character = `https://swapi-api.alx-tools.com/api/people/${charId}/`;
    const movies = JSON.parse(body).results;
    const count = movies.filter(movie => movie.characters.includes(character)).length;
    console.log(count);
  }
});
