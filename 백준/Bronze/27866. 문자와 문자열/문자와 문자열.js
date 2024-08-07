const path = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = require('fs').readFileSync(path).toString().trim().split('\n');

const word = input[0];
const num = Number(input[1]);

const answer = word[num-1]
console.log(answer);