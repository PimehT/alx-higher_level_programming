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
    let count = 0;
    for (let i = 0; i < movies.length; i++) {
      if (movies[i].characters.includes(character)) count += 1;
    }
    console.log(count);
  }
});
