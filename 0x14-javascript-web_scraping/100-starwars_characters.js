#!/usr/bin/node

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

const request = require('request');

request(apiUrl, { json: true }, (error, response, filmData) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const characterPromises = filmData.characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, { json: true }, (error, response, characterData) => {
          if (error) {
            reject(error);
          } else {
            resolve(characterData.name);
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then((characterNames) => {
        characterNames.forEach((name) => {
          console.log(name);
        });
      });
  }
});
