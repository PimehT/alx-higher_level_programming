#!/usr/bin/node
const myArray = process.argv.slice(2).map(Number);
let a = 0;
let b = 0;

if (myArray.length < 2) {
  console.log('0');
} else {
  myArray.forEach(element => {
    if (element > b) {
      a = b;
      b = element;
    } else {
      a = element > a ? element : a;
    }
  });
  console.log(a);
}
