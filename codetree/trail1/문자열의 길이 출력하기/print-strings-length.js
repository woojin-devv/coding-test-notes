const fs = require("fs");

const input = fs.readFileSync(0).toString().trim().split("\n");

let result = 0;
for (let i = 0; i < 2; i++) {
  result += input[i].length;
}

console.log(result);