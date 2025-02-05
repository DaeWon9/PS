const { dir, group } = require("console");
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

class Queue {
    constructor() {
        this.items = {};
        this.tail = 0;
        this.head = 0;
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

    size() {
        return this.tail - this.head;
    }

    get(idx) {
        if (this.head + idx >= this.tail) return undefined;
        return this.items[this.head + idx];
    }
}

const isMovable = (dr, dc) => 0 <= dr && dr < N && 0 <= dc && dc < M;

const findGroup = () => {
    let groupId = 0;
    const visited = Array.from({ length: N }, () => Array.from({ length: M }, () => false));
    const queueSize = iceQueue.size();

    for (let i = 0; i < queueSize; i++) {
        const [r, c] = iceQueue.get(i);
        if (board[r][c] === 0) {
            if (isWaterNearByIce(r, c)) waterQueue.enqueue([r, c]);
            continue;
        }

        if (visited[r][c]) continue;

        const tempIceQueue = new Queue();
        tempIceQueue.enqueue([r, c]);
        visited[r][c] = true;
        groupId++;

        while (!tempIceQueue.isEmpty()) {
            const [rr, cc] = tempIceQueue.dequeue();

            for (let i = 0; i < 4; i++) {
                const dr = rr + directionY[i];
                const dc = cc + directionX[i];

                if (isMovable(dr, dc) && board[dr][dc] !== 0 && !visited[dr][dc]) {
                    tempIceQueue.enqueue([dr, dc]);
                    visited[dr][dc] = true;
                }
            }
        }
    }

    return groupId;
};

const isWaterNearByIce = (r, c) => {
    for (let i = 0; i < 4; i++) {
        const dr = r + directionY[i];
        const dc = c + directionX[i];

        if (isMovable(dr, dc) && board[dr][dc] > 0) {
            return true;
        }
    }
    return false;
};

const meltIce = () => {
    const visited = Array.from({ length: N }, () => Array.from({ length: M }, () => false));
    const queueSize = waterQueue.size();

    for (let _ = 0; _ < queueSize; _++) {
        const [r, c] = waterQueue.dequeue();

        if (visited[r][c]) continue;

        visited[r][c] = true;
        let meltFlag = false;

        for (let i = 0; i < 4; i++) {
            const dr = r + directionY[i];
            const dc = c + directionX[i];

            if (isMovable(dr, dc) && board[dr][dc] > 0) {
                board[dr][dc]--;
                meltFlag = true;
            }
        }

        if (meltFlag) waterQueue.enqueue([r, c]);
    }
};

const directionX = [1, -1, 0, 0];
const directionY = [0, 0, 1, -1];
const [N, M] = input[0].split(" ").map(Number);
let idx = 1;
const board = [];
const waterQueue = new Queue();
const iceQueue = new Queue();

for (let i = 0; i < N; i++) {
    board.push(input[idx++].split(" ").map(Number));
}

for (let r = 0; r < N; r++) {
    for (let c = 0; c < M; c++) {
        const data = board[r][c];

        if (data === 0) {
            if (isWaterNearByIce(r, c)) waterQueue.enqueue([r, c]);
        } else {
            iceQueue.enqueue([r, c]);
        }
    }
}

let groupCount = findGroup();

if (groupCount !== 1) {
    console.log(0);
    process.exit(0);
}

let answer = 0;

while (groupCount < 2) {
    meltIce();
    groupCount = findGroup();
    answer++;
    if (groupCount === 0) {
        console.log(0);
        process.exit(0);
    }
}

console.log(answer);
