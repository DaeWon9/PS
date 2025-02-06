const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(input[0]);
const arr = input[1].split(" ").map(Number);
const copiedArr = [...new Set(arr)];
const numMap = new Map();

copiedArr.sort((a, b) => a - b);

for (let i = 0; i < copiedArr.length; i++) {
    numMap.set(copiedArr[i], i);
}

const answer = arr.map((e) => numMap.get(e));
console.log(answer.join(" "));
