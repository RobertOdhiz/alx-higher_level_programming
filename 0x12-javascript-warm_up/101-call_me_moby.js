#!/usr/bin/node
// executes x times a function

exports.theFunction = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
