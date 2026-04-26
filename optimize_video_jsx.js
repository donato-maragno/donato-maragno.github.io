const fs = require('fs');
let content = fs.readFileSync('./assets/index-YRROGjnA.js', 'utf8');

// Current: f.jsx("video", { className: "w-full h-full object-cover opacity-90", src: a, autoPlay: !0, loop: !0, muted: !0, playsInline: !0 })
// New: f.jsx("video", { className: "w-full h-full object-cover opacity-90", src: a, autoPlay: !0, loop: !0, muted: !0, playsInline: !0, preload: "metadata", poster: a.replace(".mp4", ".jpg") })

const oldPattern = ', src: a, autoPlay: !0, loop: !0, muted: !0, playsInline: !0';
const newPattern = ', src: a, autoPlay: !0, loop: !0, muted: !0, playsInline: !0, preload: "metadata", poster: a.replace(".mp4", ".jpg")';

if (content.includes(oldPattern)) {
    content = content.replace(oldPattern, newPattern);
    fs.writeFileSync('./assets/index-YRROGjnA.js', content);
    console.log('Successfully updated video component with preload and poster!');
} else {
    console.log('Pattern not found.');
}
