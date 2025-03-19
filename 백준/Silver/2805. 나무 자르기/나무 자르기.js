const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const bisectRight = (array, target) => {
    let left = 0;
    let right = array.length - 1;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);

        if (array[mid] <= target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return left;
};

const [N, M] = input[0].split(" ").map(Number);
const arr = input[1].split(" ").map(Number);
arr.sort((a, b) => a - b);

const summedArr = Array.from({ length: N }, () => 0);
summedArr[0] = arr[0];

for (let i = 1; i < N; i++) {
    summedArr[i] = summedArr[i - 1] + arr[i];
}

let left = 0;
let right = arr[N - 1];
let answer = 0;

while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const midIdx = bisectRight(arr, mid);
    const arrangeSum = midIdx == 0 ? summedArr[N - 1] : summedArr[N - 1] - summedArr[midIdx - 1];
    const cuttedHeight = arrangeSum - mid * (N - midIdx);

    if (cuttedHeight >= M) {
        answer = mid;
        left = mid + 1;
    } else {
        right = mid - 1;
    }
}

console.log(answer);
