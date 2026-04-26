const fs = require('fs');
const content = fs.readFileSync('./assets/index-YRROGjnA.js', 'utf8');

// Find the jw component again and specifically search for the experience array
const index = content.indexOf('jw = () =>');
if (index >= 0) {
    const chunk = content.substring(index, index + 10000);
    // Look for patterns like [{year:"
    const arrayMatch = chunk.match(/\[\{year:.*?\}\]/);
    if (arrayMatch) {
        console.log('--- FOUND EXPERIENCE ARRAY ---');
        console.log(arrayMatch[0]);
    } else {
        console.log('Experience array not found directly.');
        // Maybe it's defined outside?
        console.log('Component chunk start:');
        console.log(chunk.substring(0, 1000));
    }
}
