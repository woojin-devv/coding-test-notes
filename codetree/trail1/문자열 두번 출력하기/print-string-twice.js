const fs = require("fs");
let text = fs.readFileSync(0).toString().trim();

for(i = 0; i < 2; i++){
    console.log(`${text}`);
}