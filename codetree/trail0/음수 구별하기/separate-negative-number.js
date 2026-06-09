const fs = require("fs");
let num = fs.readFileSync(0).toString().trim();

if (num < 0){
    console.log(`${num} \nminus`)
} else {
    console.log(`${num}`)
}