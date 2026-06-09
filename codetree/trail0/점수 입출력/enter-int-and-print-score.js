const fs = require("fs");
let num = fs.readFileSync(0).toString().trim();

console.log(`Your score is ${num} point.`)