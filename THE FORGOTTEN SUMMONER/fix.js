const fs = require('fs');
const path = require('path');

function walkDir(dir, callback) {
    fs.readdirSync(dir).forEach(f => {
        let dirPath = path.join(dir, f);
        let isDirectory = fs.statSync(dirPath).isDirectory();
        isDirectory ? walkDir(dirPath, callback) : callback(path.join(dir, f));
    });
}

const targetDir = "C:\\Users\\Storm Credit\\Documents\\Obsidian Vault\\THE FORGOTTEN SUMMONER\\01. 아스트라리스 크로니클\\01-14. 영웅 백과 (Hero Archive)\\01-14-2. 현존 영웅\\6. 중립세력 (Neutral)";

let count = 0;
walkDir(targetDir, function(filePath) {
    if (filePath.endsWith('.md')) {
        let content = fs.readFileSync(filePath, 'utf8');
        let newContent = content.replace(/\s*\(`[A-Za-z]-[A-Za-z]` 연계\)\.*/g, '');
        if (content !== newContent) {
            fs.writeFileSync(filePath, newContent, 'utf8');
            count++;
            console.log("Fixed: " + path.basename(filePath));
        }
    }
});

console.log("Total: " + count);
