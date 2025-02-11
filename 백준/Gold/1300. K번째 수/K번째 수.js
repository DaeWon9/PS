const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

/*
i번째 행은
i, 2i, 3i, 4i, ~~
*/

const N = Number(input[0]);
const k = Number(input[1]);

let left = 0;
let right = N * N + 1;

while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    let count = 0;

    for (let i = 1; i < N + 1; i++) {
        if (i > mid) break;

        if (i === mid) {
            count++;
            break;
        }

        count += Math.min(Math.floor(mid / i), N);
    }

    if (count < k) {
        left = mid + 1;
    } else {
        right = mid - 1;
    }
}

console.log(left);
