const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

// 뻗어나가기보다, 들어오는 방식으로 생각
// target 좌표에서 좌, 우, 하 에서 최댓값들의 합을 구하면 (0, 0)에서 구해진 값이 answer

const MIN = -100001;
let idx = 1;
const [N, M] = input[0].split(" ").map(Number);
const directionR = [0, 1, 0];
const directionC = [1, 0, -1];

const board = [];
for (let i = 0; i < N; i++) {
    board.push(input[idx++].split(" ").map(Number));
}

const dp = Array.from({ length: N }, () => Array.from({ length: M }, () => Array.from({ length: 3 }, () => MIN)));
const visited = Array.from({ length: N }, () => Array.from({ length: M }, () => false));
visited[0][0] = true;

const isMovable = (r, c, N, M) => 0 <= r && r < N && 0 <= c && c < M;

const solve = (targetR, targetC, direction, N, M) => {
    if (targetR === N - 1 && targetC === M - 1) {
        return board[targetR][targetC];
    }

    // memo
    if (dp[targetR][targetC][direction] !== MIN) {
        return dp[targetR][targetC][direction];
    }

    for (let i = 0; i < 3; i++) {
        const newR = targetR + directionR[i];
        const newC = targetC + directionC[i];

        if (isMovable(newR, newC, N, M) && !visited[newR][newC]) {
            visited[newR][newC] = true;

            dp[targetR][targetC][direction] = Math.max(
                dp[targetR][targetC][direction],
                solve(newR, newC, i, N, M) + board[targetR][targetC]
            );
            // backtracking
            visited[newR][newC] = false;
        }
    }

    return dp[targetR][targetC][direction];
};

console.log(solve(0, 0, 0, N, M));
