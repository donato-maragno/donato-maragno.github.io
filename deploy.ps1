robocopy C:\Users\dmara\Desktop\personal\website\myvault\posts C:\Users\dmara\Desktop\personal\website\donatoblog\content\posts /mir

# Rebuild site
cd "C:\Users\Donato\donatoblog"
hugo

# Deploy to GitHub Pages
cd "C:\Users\Donato\donatoblog\public"
git add .
git commit -m "Update site"
git push origin main --force