const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const T = Number(input[0]);
let idx = 1;

for (let t = 0; t < T; t++) {
    const inputData = input[idx++];
    const stack = [];

    for (let data of inputData) {
        if (stack.length === 0) {
            stack.push(data);
            if (data === ")") {
                break;
            }
        } else if (stack[stack.length - 1] !== data) {
            stack.pop();
        } else {
            stack.push(data);
        }
    }

    if (stack.length === 0) {
        console.log("YES");
    } else {
        console.log("NO");
    }
}
