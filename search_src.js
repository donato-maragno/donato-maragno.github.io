const fs = require('fs');
const content = fs.readFileSync('./assets/index-YRROGjnA.js', 'utf8');

let re = /src:\s*["']\/videos\//g;
let match;
while ((match = re.exec(content)) !== null) {
    console.log('--- FOUND ---');
    console.log(content.substring(match.index - 100, match.index + 200));
}
