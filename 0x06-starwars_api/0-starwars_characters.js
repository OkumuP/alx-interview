#!/usr/bin/node

const request = require('request');

const fetchCharacterNames = (characters, index) => {
  if (index === characters.length) return;
  request(characters[index], (error, response, body) => {
    if (error) {
      throw error;
    } else {
      console.log(JSON.parse(body).name);
      fetchCharacterNames(characters, index + 1);
    }
  });
};

request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (error, response, body) => {
    if (error) {
      throw error;
    } else {
      const characterUrls = JSON.parse(body).characters;
      fetchCharacterNames(characterUrls, 0);
    }
  }
);
