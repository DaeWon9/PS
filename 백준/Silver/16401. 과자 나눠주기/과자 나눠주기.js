const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [M, N] = input[0].split(" ").map(Number);
const L = input[1].split(" ").map(Number);

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

L.sort((a, b) => a - b);

let left = 0;
let right = L[N - 1];
let answer = 0;

while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    let targetIdx = bisectLeft(L, mid);
    let biggerCount = 0;

    for (let i = N - 1; i >= targetIdx; i--) {
        biggerCount += Math.floor(L[i] / mid);
        if (biggerCount >= M) break;
    }

    if (biggerCount >= M) {
        left = mid + 1;
        answer = Math.max(answer, mid);
    } else {
        right = mid - 1;
    }
}

console.log(answer);
