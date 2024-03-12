#!/usr/bin/node

module.exports = class Rectanle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) return;

    this.width = w;

    this.height = h;
  }

  print (char = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }

  // Method to exchange the dimensions of rectangle
  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  // Method to multiply the width and height each by 2
  double () {
    this.heigth = this.height * 2;
    this.width = this.width * 2;
  }
};
