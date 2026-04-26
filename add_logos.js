const fs = require('fs');
let content = fs.readFileSync('./assets/index-YRROGjnA.js', 'utf8');

const target = 'safeguards industrial infrastructure."] })';
const logosJsx = ', f.jsx(re.div, { initial: { opacity: 0, y: 20 }, animate: { opacity: 1, y: 0 }, transition: { delay: 0.3 }, className: "flex flex-wrap items-center gap-12 mt-12 mb-16 grayscale opacity-50 hover:grayscale-0 hover:opacity-100 transition-all duration-700", children: [f.jsx("img", { src: "/images/amazon.webp", alt: "Amazon", className: "h-8 lg:h-10 object-contain" }), f.jsx("img", { src: "/images/mit.png", alt: "MIT", className: "h-10 lg:h-12 object-contain" }), f.jsx("img", { src: "/images/uva.jpg", alt: "UvA", className: "h-10 lg:h-12 object-contain rounded-sm" })] })';

if (content.includes(target)) {
    content = content.replace(target, target + logosJsx);
    fs.writeFileSync('./assets/index-YRROGjnA.js', content);
    console.log('Successfully added logos to About page!');
} else {
    console.log('Target text not found.');
}
