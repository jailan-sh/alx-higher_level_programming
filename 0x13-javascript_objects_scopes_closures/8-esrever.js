#!/usr/bin/node
exports.esrever = function (list) {
  const lReverse = [];
  let index = 0;
  for (let i = list.length - 1; i > -1; i--) {
    lReverse[index] = list[i];
    index++;
  }
  return (lReverse);
};
