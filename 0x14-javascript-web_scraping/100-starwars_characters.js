#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else if (resp.statusCode !== 200) {
    console.log(`Status: ${resp.statusCode}`);
  } else {
    const movie = JSON.parse(body);
    movie.characters.forEach(char => {
      request(char, (err, resp, body) => {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
