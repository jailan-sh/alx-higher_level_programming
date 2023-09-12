#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rec = '';
    for (let i = 0; i < this.width; i++) {
      rec += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(rec);
    }
  }
}
// const rec = 'X'; for (let i = 0; i < this.height; i++) {
// console.log(rec.repeat(this.width));}
module.exports = Rectangle;
