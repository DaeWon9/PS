const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

class MinHeap {
    constructor() {
        this.heap = [];
    }

    push([cnt, row, col]) {
        this.heap.push([cnt, row, col]);
        this.heapifyUp();
    }

    pop() {
        if (this.isEmpty()) return null;

        const root = this.heap[0];
        const lastNode = this.heap.pop();

        if (!this.isEmpty()) {
            this.heap[0] = lastNode;
            this.heapifyDown();
        }

        return root;
    }

    isEmpty() {
        return this.heap.length === 0;
    }

    heapifyUp() {
        let index = this.heap.length - 1;
        while (index > 0) {
            const parentIndex = Math.floor((index - 1) / 2);
            if (this.heap[parentIndex][0] <= this.heap[index][0]) break;
            [this.heap[parentIndex], this.heap[index]] = [this.heap[index], this.heap[parentIndex]];
            index = parentIndex;
        }
    }

    heapifyDown() {
        let index = 0;
        const length = this.heap.length;

        while (true) {
            let smallest = index;
            const leftChildIndex = 2 * index + 1;
            const rightChildIndex = 2 * index + 2;

            if (leftChildIndex < length && this.heap[leftChildIndex][0] < this.heap[smallest][0]) {
                smallest = leftChildIndex;
            }

            if (rightChildIndex < length && this.heap[rightChildIndex][0] < this.heap[smallest][0]) {
                smallest = rightChildIndex;
            }

            if (smallest === index) break;

            [this.heap[index], this.heap[smallest]] = [this.heap[smallest], this.heap[index]];
            index = smallest;
        }
    }
}

const isMovable = (dr, dc, N, M) => 0 <= dr && dr < N && 0 <= dc && dc < M;

const [M, N] = input[0].split(" ").map(Number);
const board = [];
const pq = new MinHeap();
const counts = Array.from({ length: N }, () => Array(M).fill(2147483647));

for (let i = 0; i < N; i++) {
    board.push(input[i + 1].split("").map(Number));
}

pq.push([0, 0, 0]);
counts[0][0] = 0;

while (!pq.isEmpty()) {
    const node = pq.pop();
    if (!node) break;
    const [cnt, row, col] = node;

    if (row === N - 1 && col === M - 1) {
        console.log(cnt);
        break;
    }

    for (let i = 0; i < 4; i++) {
        const dr = row + [1, -1, 0, 0][i];
        const dc = col + [0, 0, 1, -1][i];

        if (isMovable(dr, dc, N, M)) {
            const newCost = cnt + board[dr][dc];
            if (counts[dr][dc] > newCost) {
                counts[dr][dc] = newCost;
                pq.push([newCost, dr, dc]);
            }
        }
    }
}
