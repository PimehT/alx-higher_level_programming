#!/usr/bin/node
const myNum = parseInt(process.argv[2]);

function factorial (myNum) {
  let result = 1;

  if (isNaN(myNum)) {
    return (1);
  } else if (myNum === 1) {
    return (result);
  } else {
    result = myNum;
    return (result * factorial(myNum - 1));
  }
}

console.log(factorial(myNum));
