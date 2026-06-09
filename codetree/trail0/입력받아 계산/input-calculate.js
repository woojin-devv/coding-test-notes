const fs = require("fs");
let a = fs.readFileSync(0).toString().trim();

console.log(`${Number(a)+2}`);
