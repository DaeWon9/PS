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

function isMovable(dx, dy) {
    return 0 <= dx && dx < N && 0 <= dy && dy < M;
}

const [N, M] = input[0].split(" ").map(Number);
const [Hx, Hy] = input[1].split(" ").map(Number);
const [Ex, Ey] = input[2].split(" ").map(Number);
let idx = 3;
const directionX = [0, 0, 1, -1];
const directionY = [1, -1, 0, 0];
const visited = Array.from({ length: 2 }, () => Array.from({ length: N }, () => Array.from({ length: M }, () => 0)));

const board = [];
for (let i = 0; i < N; i++) {
    board.push(input[idx++].split(" ").map(Number));
}

const queue = new Queue();
queue.enqueue([Hx - 1, Hy - 1, 0, 0]);

while (!queue.isEmpty()) {
    const [x, y, dist, flag] = queue.dequeue();

    if (x === Ex - 1 && y === Ey - 1) {
        console.log(dist);
        return;
    }

    for (let i = 0; i < 4; i++) {
        const dx = x + directionX[i];
        const dy = y + directionY[i];

        if (!isMovable(dx, dy)) continue;

        if (board[dx][dy] === 1 && flag === 0 && visited[1][dx][dy] === 0) {
            visited[1][dx][dy] = 1;
            queue.enqueue([dx, dy, dist + 1, 1]);
        } else if (board[dx][dy] === 0 && visited[flag][dx][dy] === 0) {
            visited[flag][dx][dy] = 1;
            queue.enqueue([dx, dy, dist + 1, flag]);
        }
    }
}

console.log(-1);
