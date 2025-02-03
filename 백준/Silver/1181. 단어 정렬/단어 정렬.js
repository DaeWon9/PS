const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(input[0]);
let idx = 1;
let words = [];

for (let i = 0; i < N; i++) {
    words.push(input[idx++]);
}

let uniqueWords = [...new Set(words)];

uniqueWords.sort((a, b) => {
    if (a.length === b.length) return a.localeCompare(b);
    return a.length - b.length;
});

console.log(uniqueWords.join("\n"));
