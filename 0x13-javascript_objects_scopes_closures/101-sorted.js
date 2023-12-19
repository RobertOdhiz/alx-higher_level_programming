#!/usr/bin/node
// ...

const { dict } = require('./101-data');

const invertedDict = {};

Object.keys(dict).map(userId => {
  const occurrences = dict[userId];

  invertedDict[occurrences] = invertedDict[occurrences] || [];
  invertedDict[occurrences].push(userId.toString());
});

console.log(invertedDict);
