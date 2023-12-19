#!/usr/bin/node
// imports an array and computes a new array

const original = require('./100-data').list;
console.log(original);
const mappedList = original.map((e, index) => {
  return (e * index);
});
console.log(mappedList);
