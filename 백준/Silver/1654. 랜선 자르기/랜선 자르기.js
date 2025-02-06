const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [K, N] = input[0].split(" ").map(Number);
const arr = [];
let idx = 1;

const bisectLeft = (arr, target) => {
    let left = 0;
    let right = arr.length - 1;
    let mid = 0;

    while (left <= right) {
        mid = Math.floor((left + right) / 2);

        if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return mid;
};

for (let i = 0; i < K; i++) {
    arr.push(Number(input[idx++]));
}

arr.sort((a, b) => a - b);

let left = 0;
let right = arr[K - 1];
let answer = 0;

while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    let curIdx = bisectLeft(arr, mid);
    let possibleCount = 0;

    for (let i = K - 1; i >= curIdx; i--) {
        possibleCount += Math.floor(arr[i] / mid);
        if (possibleCount >= N) break;
    }

    if (possibleCount >= N) {
        left = mid + 1;
        answer = Math.max(answer, mid);
    } else {
        right = mid - 1;
    }
}

console.log(answer);
