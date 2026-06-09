const fs = require("fs");
let N = fs.readFileSync(0).toString().trim();

console.log(`${Number(N).toFixed(2)}`);