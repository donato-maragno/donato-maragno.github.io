const fs = require('fs');
const content = fs.readFileSync('./assets/index-YRROGjnA.js', 'utf8');

// The JSX call is f.jsx(Ci, {src: ...})
// So Ci is likely a component defined like Ci=(...) or const Ci = (...)
// In React production builds, names are often short.

// Let's find where Ci is defined. 
// We can search for ",Ci=" or "{Ci=" or "const Ci="

const targets = [',Ci=', '{Ci=', 'const Ci=', 'var Ci='];
targets.forEach(t => {
    let index = content.indexOf(t);
    if (index >= 0) {
        console.log(`--- FOUND ${t} ---`);
        console.log(content.substring(index, index + 500));
    }
});
