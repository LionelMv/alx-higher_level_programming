#!/usr/bin/node

const numsArray = process.argv.slice(2);

function findSecondLargestInteger (arr) {
  if (arr.length < 2) {
    return (0);
  } else {
    let largest = Number.NEGATIVE_INFINITY;
    let secondLargest = Number.NEGATIVE_INFINITY;

    for (const num of arr) {
      if (num > largest) {
        secondLargest = largest;
        largest = num;
      } else if (num > secondLargest && num < largest) {
        secondLargest = num;
      }
    }
    return secondLargest;
  }
}

console.log(findSecondLargestInteger(numsArray));
