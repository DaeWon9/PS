const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

class Queue {
    constructor() {
        this.items = {};
        this.head = 0;
        this.tail = 0;
    }

    isEmpty() {
        return this.tail === this.head;
    }

    append(e) {
        this.items[this.tail++] = e;
    }

    pop() {
        if (this.isEmpty()) return undefined;
        const item = this.items[this.head];
        delete this.items[this.head];
        this.head++;
        return item;
    }
}

const [N, M] = input[0].split(" ").map(Number);
let idx = 1;
const adj_vertices = Array.from({ length: N + 1 }, () => []);

for (let i = 0; i < N - 1; i++) {
    const [v1, v2, d] = input[idx++].split(" ").map(Number);
    adj_vertices[v1].push([v2, d]);
    adj_vertices[v2].push([v1, d]);
}

for (let m = 0; m < M; m++) {
    const [v1, v2] = input[idx++].split(" ").map(Number);
    const queue = new Queue();
    const visited = new Set();
    visited.add(v1);
    queue.append([v1, 0]);

    while (!queue.isEmpty()) {
        const [v, d] = queue.pop();

        if (v === v2) {
            console.log(d);
            break;
        }

        for (const [adj_vertex, dist] of adj_vertices[v]) {
            if (visited.has(adj_vertex)) {
                continue;
            }

            queue.append([adj_vertex, d + dist]);
            visited.add(adj_vertex);
        }
    }
}
