#!/usr/bin/node

const BaseSquare = require('./5-sqaure');

class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i += 1) {
        console.log(c.repeat(this.height));
      }
    }
  }
}
module.exports = Square;
