const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const lessonTimes = input[1].split(" ").map(Number);

let left = 10001;
let right = 1;
let answer = 0;

for (const time of lessonTimes) {
    if (left > time) {
        left = time;
    }
    right += time;
}

while (left <= right) {
    const size = Math.floor((left + right) / 2);
    let count = 1;
    let tempSum = 0;
    let possibleFlag = true;

    for (const time of lessonTimes) {
        if (time > size) {
            possibleFlag = false;
            break;
        }

        if (tempSum + time > size) {
            tempSum = time;
            count++;
        } else {
            tempSum += time;
        }
    }

    if (!possibleFlag) {
        left = size + 1;
        continue;
    }

    if (count <= M) {
        right = size - 1;
        answer = size;
    } else {
        left = size + 1;
    }
}

console.log(answer);
