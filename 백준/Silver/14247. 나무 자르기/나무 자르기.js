const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

// 최대한 키운다

const n = Number(input[0]);
const init = input[1].split(" ").map(Number);
const grow = input[2].split(" ").map(Number);
let answer = 0;

const tree = [];
for (let i = 0; i < n; i++) {
    tree.push([init[i], grow[i]]);
}

tree.sort((a, b) => b[1] - a[1]);

for (let i = n - 1; i >= 0; i--) {
    const [h, g] = tree[n - 1 - i];
    answer += g * i + h;
}

console.log(answer);
