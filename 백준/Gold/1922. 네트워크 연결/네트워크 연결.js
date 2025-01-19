const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

function find(x) {
    if (parent[x] === x) {
        return x;
    }

    parent[x] = find(parent[x]);
    return parent[x];
}

function union(x, y) {
    x = find(x);
    y = find(y);

    if (x === y) return;

    if (x < y) {
        parent[y] = x;
    } else {
        parent[x] = y;
    }
}

N = Number(input[0]);
M = Number(input[1]);
let idx = 2;
let answer = 0;
const infoList = [];
const parent = Array.from({ length: N + 1 }, (_, i) => i);

for (let i = 0; i < M; i++) {
    const [u, v, c] = input[idx++].split(" ").map(Number);
    infoList.push([c, u, v]);
}

infoList.sort((a, b) => a[0] - b[0]);

for (const [c, u, v] of infoList) {
    if (find(u) !== find(v)) {
        union(u, v);
        answer += c;
    }
}

console.log(answer);
