const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

// 더하다가 연속합 보다 자신이 큰 경우 처리
const n = Number(input[0]);
const arr = input[1].split(" ").map(Number);

let summedArr = Array.from({ length: n }, () => 0);
summedArr[0] = arr[0];
let answer = arr[0];

for (let i = 1; i < n; i++) {
    const newValue = summedArr[i - 1] + arr[i];

    if (newValue <= arr[i]) {
        summedArr[i] = arr[i];
        answer = Math.max(answer, arr[i]);
    } else {
        summedArr[i] = newValue;
        answer = Math.max(answer, newValue);
    }
}

console.log(answer);
