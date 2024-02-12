#!/usr/bin/node
const myNum = parseInt(process.argv[2]);

let count = 0;
if (!(myNum)) {
  console.log('Missing number of occurrences');
} else {
  while (count < myNum) {
    console.log('C is fun');
    count++;
  }
}
