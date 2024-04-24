#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const baseUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function fetchData (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

fetchData(baseUrl)
  .then((movie) => {
    const characters = movie.characters;
    characters.forEach(async (char) => {
      try {
        const character = await fetchData(char);
        console.log(character.name);
      } catch (error) {
        console.log(error);
      }
    });
  })
  .catch((error) => {
    console.log(error);
  });
