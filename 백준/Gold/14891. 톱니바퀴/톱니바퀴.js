const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

class Queue {
    constructor() {
        this.items = {};
        this.head = 0;
        this.tail = 0;
    }

    append(e) {
        this.items[this.tail++] = e;
    }

    pop() {
        const item = this.items[this.head];
        delete this.items[this.head];
        this.head++;
        return item;
    }

    isEmpty() {
        return this.head === this.tail;
    }
}

function rotate(array, k) {
    const n = array.length;
    k = ((k % n) + n) % n;
    return [...array.slice(-k), ...array.slice(0, -k)];
}

const TOP = 0;
const LEFT = 6;
const RIGHT = 2;
let idx = 0;
const wheelInfos = [];

for (let i = 0; i < 4; i++) {
    wheelInfos.push(input[idx++]);
}

const K = input[idx++];

for (let k = 0; k < K; k++) {
    let [targetIdx, dir] = input[idx++].split(" ").map(Number);
    const actionQueue = new Queue();

    targetIdx--;
    actionQueue.append([targetIdx, dir]);

    // check right side
    for (let i = targetIdx; i < 3; i++) {
        if (wheelInfos[i][RIGHT] === wheelInfos[i + 1][LEFT]) {
            break;
        }

        if (targetIdx % 2 === i % 2) {
            actionQueue.append([i + 1, -dir]);
        } else {
            actionQueue.append([i + 1, dir]);
        }
    }

    // check left side
    for (let i = targetIdx; i > 0; i--) {
        if (wheelInfos[i][LEFT] === wheelInfos[i - 1][RIGHT]) {
            break;
        }

        if (targetIdx % 2 === i % 2) {
            actionQueue.append([i - 1, -dir]);
        } else {
            actionQueue.append([i - 1, dir]);
        }
    }

    while (!actionQueue.isEmpty()) {
        const [targetIdx, dir] = actionQueue.pop();
        wheelInfos[targetIdx] = rotate(wheelInfos[targetIdx], dir);
    }
}

let answer = 0;
if (wheelInfos[0][TOP] === "1") {
    answer += 1;
}
if (wheelInfos[1][TOP] === "1") {
    answer += 2;
}
if (wheelInfos[2][TOP] === "1") {
    answer += 4;
}
if (wheelInfos[3][TOP] === "1") {
    answer += 8;
}

console.log(answer);
