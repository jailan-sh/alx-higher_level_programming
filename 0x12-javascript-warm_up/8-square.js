#!/usr/bin/node

if (Number(process.argv[2])) {
  for (let x = 0; x < Number(process.argv[2]); x++) {
    for (let j = 0; j < Number(process.argv[2]); j++) {
      console.log('x');
    }
  }
} else {
  console.log('Missing sizes');
}
