const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const LEFT = 0;
const DOWN = 1;
const RIGHT = 2;
const UP = 3;

const N = Number(input[0]);
const board = [];
let row = Math.floor(N / 2);
let col = row;
let direction = 0;
let pathLength = 1;
let moveCount = 0;
let answer = 0;

const directionC = [-1, 0, 1, 0];
const directionR = [0, 1, 0, -1];

for (let i = 1; i <= N; i++) {
    board.push(input[i].split(" ").map(Number));
}

function isMovable(dr, dc) {
    return 0 <= dr && dr < N && 0 <= dc && dc < N;
}

function spreadSand(row, col, direction) {
    const sandAmount = board[row][col];
    board[row][col] = 0;

    const amount1Percent = Math.floor(sandAmount * 0.01);
    const amount2Percent = Math.floor(sandAmount * 0.02);
    const amount5Percent = Math.floor(sandAmount * 0.05);
    const amount7Percent = Math.floor(sandAmount * 0.07);
    const amount10Percent = Math.floor(sandAmount * 0.1);

    const totalSpread =
        amount1Percent * 2 + amount2Percent * 2 + amount5Percent + amount7Percent * 2 + amount10Percent * 2;

    const remainSandAmount = sandAmount - totalSpread;

    let directions = [
        [-1, 1, amount1Percent],
        [1, 1, amount1Percent], // 1%
        [-2, 0, amount2Percent],
        [2, 0, amount2Percent], // 2%
        [-1, 0, amount7Percent],
        [1, 0, amount7Percent], // 7%
        [-1, -1, amount10Percent],
        [1, -1, amount10Percent], // 10%
        [0, -2, amount5Percent], // 5%
        [0, -1, remainSandAmount], // a
    ];

    switch (direction) {
        case LEFT:
            break;
        case DOWN:
            directions = directions.map(([r, c, v]) => [-c, r, v]);
            break;
        case RIGHT:
            directions = directions.map(([r, c, v]) => [r, -c, v]);
            break;
        case UP:
            directions = directions.map(([r, c, v]) => [c, -r, v]);
            break;
    }

    for (let i = 0; i < directions.length; i++) {
        const dr = row + directions[i][0];
        const dc = col + directions[i][1];
        let value = directions[i][2];

        if (isMovable(dr, dc)) board[dr][dc] += value;
        else answer += value;
    }
}

while (true) {
    if (row === 0 && col === 0) break;

    if (moveCount === 2) {
        pathLength++;
        moveCount = 0;
    }

    for (let i = 0; i < pathLength; i++) {
        row += directionR[direction];
        col += directionC[direction];

        spreadSand(row, col, direction);

        if (row === 0 && col === 0) break;
    }

    moveCount++;
    direction = (direction + 1) % 4;
}

console.log(answer);
