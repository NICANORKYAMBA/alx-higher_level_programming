#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;
let count = 0;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body);

  for (let i = 0; i < data.results.length; i++) {
    const film = data.results[i];

    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      count++;
    }
  }

  console.log(count);
});
