#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const size = process.argv.length;
  const myArg = [];
  for (let i = 2; i < size; i++) {
    myArg[i - 2] = Number(process.argv[i]);
  }
  myArg.sort(function (a, b) { return b - a; });
  console.log(myArg[1]);
}
