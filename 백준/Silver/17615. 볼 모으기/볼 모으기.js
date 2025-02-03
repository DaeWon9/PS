const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(input[0]);
const inputData = input[1];

const firstChar = inputData[0];
const lastChar = inputData[N - 1];
let firstGroupFlag = false;

let RCenterCount = 0;
let BCenterCount = 0;
let firstGroupCount = 1;
let lastGroupCount = 0;
let prevChar = firstChar;
let tempCount = 0;

for (let i = 1; i < N; i++) {
    if (!firstGroupFlag) {
        if (inputData[i] === firstChar) {
            firstGroupCount++;
        } else {
            firstGroupFlag = true;
            prevChar = inputData[i];
            tempCount = 1;
            if (inputData[i] === "R") RCenterCount++;
            else BCenterCount++;
        }
        continue;
    }

    if (inputData[i] === "R") RCenterCount++;
    else BCenterCount++;

    if (prevChar === inputData[i]) {
        tempCount++;
    } else {
        prevChar = inputData[i];
        tempCount = 1;
    }
}
lastGroupCount = tempCount;

if (lastChar === "R") {
    RCenterCount -= lastGroupCount;
} else {
    BCenterCount -= lastGroupCount;
}

let answer = 2147483647;

if (lastChar === "R") {
    answer = Math.min(
        answer,
        RCenterCount + (firstChar === "R" ? firstGroupCount : 0),
        BCenterCount + (firstChar === "B" ? firstGroupCount : 0) + (lastChar === "B" ? lastGroupCount : 0)
    );
} else {
    answer = Math.min(
        answer,
        BCenterCount + (firstChar === "B" ? firstGroupCount : 0),
        RCenterCount + (firstChar === "R" ? firstGroupCount : 0) + (lastChar === "R" ? lastGroupCount : 0)
    );
}

if (firstChar === "R") {
    answer = Math.min(
        answer,
        RCenterCount + (lastChar === "R" ? lastGroupCount : 0),
        BCenterCount + (firstChar === "B" ? firstGroupCount : 0) + (lastChar === "B" ? lastGroupCount : 0)
    );
} else {
    answer = Math.min(
        answer,
        BCenterCount + (lastChar === "B" ? lastGroupCount : 0),
        RCenterCount + (firstChar === "R" ? firstGroupCount : 0) + (lastChar === "R" ? lastGroupCount : 0)
    );
}

console.log(answer);
