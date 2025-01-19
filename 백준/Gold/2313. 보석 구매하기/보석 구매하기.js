const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const n = Number(input[0]);
let tc = 0;
let result_sum = 0;
const result_range = [];

for (let i = 0; i < n; i++) {
    const L = Number(input[i + tc + 1]);
    let arr = input[i + tc + 2].split(" ").map(Number);
    tc++;

    let maxSum = arr[0];
    let maxL = 0;
    let maxR = 0;
    let l = 0;
    let r = 0;

    for (let j = 0; j < L; j++) {
        if (arr[j] < arr[j - 1] + arr[j]) {
            arr[j] += arr[j - 1];
            r = j;
        } else {
            l = j;
            r = j;
        }

        if (maxSum < arr[j]) {
            maxSum = arr[j];
            maxL = l;
            maxR = r;
        } else if (maxSum === arr[j]) {
            const prevCount = maxR - maxL;
            const newCount = r - l;

            if (prevCount > newCount) {
                maxL = l;
                maxR = r;
            }
        }
    }

    result_sum += maxSum;
    result_range.push([maxL + 1, maxR + 1]);
}

console.log(result_sum);
for (range of result_range) {
    console.log(range.join(" "));
}
