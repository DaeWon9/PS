const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

class Queue {
    constructor() {
        this.items = {};
        this.head = 0;
        this.tail = 0;
    }

    enqueue(e) {
        this.items[this.tail++] = e;
    }

    dequeue() {
        const item = this.items[this.head];
        delete this.items[this.head];
        this.head++;
        return item;
    }

    isEmpty() {
        return this.head === this.tail;
    }
}

function isMovable(R, C, dr, dc) {
    return 0 <= dr && dr < R && 0 <= dc && dc < C;
}

const T = Number(input[0]);
let idx = 1;
const directionX = [1, -1, 0, 0];
const directionY = [0, 0, 1, -1];

for (let t = 0; t < T; t++) {
    const [C, R, K] = input[idx++].split(" ").map(Number);
    const queue = new Queue();
    const visited = Array.from({ length: R }, () => Array.from({ length: C }, () => false));
    const board = Array.from({ length: R }, () => Array.from({ length: C }, () => 0));
    let answer = 0;

    for (let k = 0; k < K; k++) {
        const [c, r] = input[idx++].split(" ").map(Number);
        board[r][c] = 1;

        queue.enqueue([r, c]);
    }

    while (!queue.isEmpty()) {
        const [r, c] = queue.dequeue();

        if (visited[r][c]) continue;

        answer++;

        const subQueue = new Queue();
        subQueue.enqueue([r, c]);

        while (!subQueue.isEmpty()) {
            const [rr, cc] = subQueue.dequeue();

            for (let i = 0; i < 4; i++) {
                const dr = rr + directionY[i];
                const dc = cc + directionX[i];

                if (isMovable(R, C, dr, dc) && board[dr][dc] === 1 && !visited[dr][dc]) {
                    subQueue.enqueue([dr, dc]);
                    visited[dr][dc] = true;
                }
            }
        }
    }

    console.log(answer);
}
