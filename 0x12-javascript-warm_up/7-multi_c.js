#!/usr/bin/node

if (Number(process.argv[2])) {
  let x = 0;
  while (x < Number(process.argv[2])) {
    console.log('C is fun');
    x++;
  }
} else {
  console.log('Missing number of occurrences');
}
