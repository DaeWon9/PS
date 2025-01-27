const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const isMovable = (dr, dc, H, W) => dr >= 0 && dr < H && dc >= 0 && dc < W;

const directionX = [1, -1, 0, 0];
const directionY = [0, 0, 1, -1];

const [W, H] = input[0].split(" ").map(Number);
const CPosList = [];
const board = [];

for (let r = 0; r < H; r++) {
  const inputData = input[r + 1];
  for (let c = 0; c < inputData.length; c++) {
    if (inputData[c] === "C") {
      CPosList.push([r, c]);
    }
  }
  board.push(inputData);
}

const [startPos, endPos] = CPosList;

const queue = [];
queue.push([startPos[0], startPos[1], -1, 0]);
const mirrorCount = Array.from({ length: 4 }, () =>
  Array.from({ length: H }, () => Array(W).fill(9999))
);

for (let i = 0; i < 4; i++) {
  mirrorCount[i][startPos[0]][startPos[1]] = 0;
}

while (queue.length > 0) {
  const [r, c, p, cnt] = queue.shift();

  if (mirrorCount[p]?.[r]?.[c] < cnt) continue;

  for (let i = 0; i < 4; i++) {
    const dr = r + directionY[i];
    const dc = c + directionX[i];

    if (!isMovable(dr, dc, H, W)) continue;
    if (board[dr][dc] === "*") continue;

    if ((p === -1 || p === i) && mirrorCount[i][dr][dc] > cnt) {
      mirrorCount[i][dr][dc] = cnt;
      queue.push([dr, dc, i, cnt]);
    } else if (mirrorCount[i][dr][dc] > cnt + 1) {
      mirrorCount[i][dr][dc] = cnt + 1;
      queue.push([dr, dc, i, cnt + 1]);
    }
  }
}

const answer = Math.min(
  mirrorCount[0][endPos[0]][endPos[1]],
  mirrorCount[1][endPos[0]][endPos[1]],
  mirrorCount[2][endPos[0]][endPos[1]],
  mirrorCount[3][endPos[0]][endPos[1]]
);

console.log(answer);
