#!/usr/bin/node
// Square class that inherits from 4-rectangle.js Rectangle

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
