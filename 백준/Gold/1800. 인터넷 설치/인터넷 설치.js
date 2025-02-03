const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const INF = Number.MAX_SAFE_INTEGER;
const [n, p, k] = input[0].split(" ").map(Number);
const nodes = Array.from({ length: n + 1 }, () => []);
let maxCost = 0;

for (let i = 1; i <= p; i++) {
    const [a, b, c] = input[i].split(" ").map(Number);
    nodes[a].push([b, c]);
    nodes[b].push([a, c]);
    maxCost = Math.max(maxCost, c);
}

function dijkstra(costBudget) {
    const distances = new Array(n + 1).fill(INF);
    distances[1] = 0;
    let queue = [[0, 1]];

    while (queue.length) {
        queue.sort((a, b) => a[0] - b[0]);
        const [curCost, curNode] = queue.shift();

        if (distances[curNode] < curCost) continue;

        for (const [nextNode, nextCost] of nodes[curNode]) {
            if (costBudget < nextCost) {
                if (distances[nextNode] > curCost + 1) {
                    distances[nextNode] = curCost + 1;
                    queue.push([curCost + 1, nextNode]);
                }
            } else {
                if (distances[nextNode] > curCost) {
                    distances[nextNode] = curCost;
                    queue.push([curCost, nextNode]);
                }
            }
        }
    }
    return distances[n];
}

let left = 0,
    right = maxCost,
    answer = INF;
while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (dijkstra(mid) <= k) {
        right = mid - 1;
        answer = mid;
    } else {
        left = mid + 1;
    }
}

console.log(answer === INF ? -1 : answer);
