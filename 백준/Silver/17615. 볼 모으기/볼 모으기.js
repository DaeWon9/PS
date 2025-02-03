const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(input[0]);
const inputData = input[1];

const lastChar = inputData[inputData.length - 1];
const firstCahr = inputData[0];
const RGroup = inputData.split("B").filter((item) => item);
const BGroup = inputData.split("R").filter((item) => item);

if (RGroup.length === 0 || BGroup.length === 0 || (RGroup.length === 1 && BGroup.length === 1)) {
    console.log(0);
    process.exit(0);
}

let RCenterCount = 0;
let BCenterCount = 0;
let answer = 2147483647;

for (const data of RGroup.slice(1, RGroup.length - 1)) {
    RCenterCount += data.length;
}

for (const data of BGroup.slice(1, BGroup.length - 1)) {
    BCenterCount += data.length;
}

if (firstCahr === "R") {
    answer = Math.min(
        answer,
        RCenterCount + RGroup[RGroup.length - 1].length,
        BCenterCount + BGroup[0].length + BGroup[BGroup.length - 1].length
    );
} else {
    answer = Math.min(
        answer,
        BCenterCount + BGroup[BGroup.length - 1].length,
        RCenterCount + RGroup[0].length + RGroup[RGroup.length - 1].length
    );
}

if (lastChar === "R") {
    answer = Math.min(
        answer,
        RCenterCount + RGroup[0].length,
        BCenterCount + BGroup[0].length + BGroup[BGroup.length - 1].length
    );
} else {
    answer = Math.min(
        answer,
        BCenterCount + BGroup[0].length,
        RCenterCount + RGroup[0].length + RGroup[RGroup.length - 1].length
    );
}

console.log(answer);
