const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

class Queue {
    constructor() {
        this.items = {};
        this.head = 0;
        this.tail = 0;
    }

    push(e) {
        this.items[this.tail++] = e;
    }

    pop() {
        const item = this.items[this.head];
        delete this.items[this.head];
        this.head++;
        return item;
    }

    isEmpty() {
        return this.tail === this.head;
    }
}

function isMovable(dr, dc) {
    return 0 <= dr && dr < N && 0 <= dc && dc < M;
}

let idx = 1;
let answer = -1;
const directionX = [0, 0, 1, -1];
const directionY = [1, -1, 0, 0];
const [N, M] = input[0].split(" ").map(Number);
const queue = new Queue();
const visited = Array.from({ length: 2 }, () => Array.from({ length: N }, () => Array.from({ length: M }, () => 0)));
const board = [];
for (let r = 0; r < N; r++) {
    board.push(input[idx++].split("").map(Number));
}

queue.push([0, 0, 0]);
visited[0][0][0] = 1;

while (!queue.isEmpty()) {
    const [row, col, flag] = queue.pop();

    if (row === N - 1 && col === M - 1) {
        answer = visited[flag][row][col];
        break;
    }

    for (let i = 0; i < 4; i++) {
        const dr = row + directionY[i];
        const dc = col + directionX[i];

        if (!isMovable(dr, dc)) continue;

        if (board[dr][dc] === 1 && flag === 0) {
            visited[1][dr][dc] = visited[0][row][col] + 1;
            queue.push([dr, dc, 1]);
        } else if (board[dr][dc] === 0 && visited[flag][dr][dc] === 0) {
            visited[flag][dr][dc] = visited[flag][row][col] + 1;
            queue.push([dr, dc, flag]);
        }
    }
}

console.log(answer);
