const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const inputData = input[0];
const stack = [];
let numStack = [];
let closeFlag = false;
let possibleFlag = true;
let answer = 0;

for (let i = 0; i < inputData.length; i++) {
    const data = inputData[i];
    if (stack.length === 0) {
        // 올바르지 않은 괄호
        if (data === ")" || data === "]") {
            possibleFlag = false;
            break;
        }

        stack.push([i, data]);
        closeFlag = false;
        continue;
    }

    if (data === "(" || data === "[") {
        stack.push([i, data]);
        closeFlag = false;
    } else if (data === ")") {
        const [topIndex, topData] = stack[stack.length - 1];
        if (topData !== "(") {
            possibleFlag = false;
            break;
        }

        let tempSum = 0;

        while (1) {
            if (numStack.length === 0) break;

            if (numStack[numStack.length - 1][0] >= topIndex) {
                const popedData = numStack.pop();
                tempSum += popedData[1];
            } else {
                break;
            }
        }

        tempSum = tempSum === 0 ? 1 : tempSum;

        if (stack.length === 1) {
            answer += tempSum * 2;
            numStack = [];
            closeFlag = true;
            stack.pop();
            continue;
        }

        stack.pop();

        if (closeFlag) {
            numStack.push([topIndex, tempSum * 2]);
        } else {
            numStack.push([i, 2]);
        }

        closeFlag = true;
    } else {
        const [topIndex, topData] = stack[stack.length - 1];
        if (topData !== "[") {
            possibleFlag = false;
            break;
        }

        let tempSum = 0;

        while (1) {
            if (numStack.length === 0) break;

            if (numStack[numStack.length - 1][0] >= topIndex) {
                const popedData = numStack.pop();
                tempSum += popedData[1];
            } else {
                break;
            }
        }

        tempSum = tempSum === 0 ? 1 : tempSum;

        if (stack.length === 1) {
            answer += tempSum * 3;
            numStack = [];
            closeFlag = true;
            stack.pop();
            continue;
        }

        stack.pop();

        if (closeFlag) {
            numStack.push([topIndex, tempSum * 3]);
        } else {
            numStack.push([i, 3]);
        }

        closeFlag = true;
    }
}

if (stack.length > 0 || !possibleFlag) {
    console.log(0);
} else {
    console.log(answer);
}
