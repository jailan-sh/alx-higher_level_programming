#!/usr/bin/node

if (Number(process.argv[2])) {
  const size = Number(process.argv[2]);
  let i = 0;
  while (i < size) {
    let j = 0;
    let row = '';
    while (j < size) {
      row += 'X';
      j++;
    }
    console.log(row);
    i++;
  }
} else {
  console.log('Missing size');
}
