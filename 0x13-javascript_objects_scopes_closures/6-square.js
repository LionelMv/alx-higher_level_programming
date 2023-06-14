#!/usr/bin/node

const BaseSquare = require('5-sqaure');
class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.size; i += 1) {
        console.log(c.repeat(this.size));
      }
    }
  }
}
module.exports = Square;
