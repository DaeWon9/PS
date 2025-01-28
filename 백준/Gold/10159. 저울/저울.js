const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const N = Number(input[0]);
const M = Number(input[1]);
let idx = 2;

const adj_matrix = Array.from({ length: N + 1 }, () => Array.from({ length: N + 1 }, () => 0));

for (let i = 0; i < M; i++) {
    const [u, v] = input[idx++].split(" ").map(Number);
    adj_matrix[u][v] = 1;
}

for (let k = 1; k < N + 1; k++) {
    for (let i = 1; i < N + 1; i++) {
        for (let j = 1; j < N + 1; j++) {
            if (adj_matrix[i][k] !== 0 && adj_matrix[k][j] !== 0) {
                adj_matrix[i][j] = 1;
            }
        }
    }
}
for (let i = 1; i < N + 1; i++) {
    let cnt = 0;
    for (let j = 1; j < N + 1; j++) {
        if (i === j) continue;

        if (adj_matrix[i][j] === 0 && adj_matrix[j][i] === 0) {
            cnt++;
        }
    }
    console.log(cnt);
}
