#!/usr/bin/node
const myNum = parseInt(process.argv[2]);

if (isNaN(myNum)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myNum; i++) {
    let row = '';
    for (let j = 0; j < myNum; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
