const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

function getIndex(row, col) {
    return row * n + col;
}

function isMovable(dr, dc) {
    return 0 <= dr && dr < n && 0 <= dc && dc < n;
}

function solve(row, col) {
    const targetIndex = getIndex(row, col);

    if (memo.has(targetIndex)) return memo.get(targetIndex);

    memo.set(targetIndex, 1);
    for (let i = 0; i < 4; i++) {
        let dr = row + directionY[i];
        let dc = col + directionX[i];

        if (isMovable(dr, dc) && board[row][col] < board[dr][dc]) {
            memo.set(targetIndex, Math.max(memo.get(targetIndex), solve(dr, dc) + 1));
        }
    }

    return memo.get(targetIndex);
}

const n = Number(input[0]);
const memo = new Map();
const directionX = [0, 0, 1, -1];
const directionY = [1, -1, 0, 0];
let idx = 1;
let answer = 0;
const board = [];
for (let i = 0; i < n; i++) {
    board.push(input[idx++].split(" ").map(Number));
}

for (let r = 0; r < n; r++) {
    for (let c = 0; c < n; c++) {
        answer = Math.max(answer, solve(r, c));
    }
}

console.log(answer);
