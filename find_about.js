const fs = require('fs');
const content = fs.readFileSync('./assets/index-YRROGjnA.js', 'utf8');

// Find the component associated with /about
// Pattern: path: "/about", element: f.jsx(Zw, {})
const re = /path:\s*["']\/about["'],\s*element:\s*f\.jsx\(([a-zA-Z0-9]+)/;
const match = content.match(re);
if (match) {
    console.log('--- FOUND ABOUT COMPONENT ---');
    console.log('Component name: ' + match[1]);
    
    // Now find the definition of match[1]
    const compName = match[1];
    const compDefRe = new RegExp(compName + '\\s*=\\s*\\(\\)\\s*=>', 'g');
    let defMatch;
    while ((defMatch = compDefRe.exec(content)) !== null) {
        console.log('--- DEFINITION AT --- ' + defMatch.index);
        console.log(content.substring(defMatch.index, defMatch.index + 2000));
    }
} else {
    console.log('About route not found.');
}
