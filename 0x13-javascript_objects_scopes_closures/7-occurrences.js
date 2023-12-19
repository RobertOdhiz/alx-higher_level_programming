#!/usr/bin/node
// function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let flag = 0;

  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      flag += 1;
    }
  }

  return flag;
};
