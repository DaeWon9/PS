const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const calc_score = (prev, next) => {
    if (prev === 0) return 2;
    if (prev === next) return 1;
    if (Math.abs(prev - next) === 2) return 4;
    return 3;
};

const INF = 444444;
const arr = input[0].split(" ").map(Number);
const dp = Array.from({ length: arr.length + 1 }, () => Array.from({ length: 5 }, () => Array(5).fill(INF)));
let lastData = 0;
dp[0][0][0] = 0;

for (let i = 1; i <= arr.length; i++) {
    const data = arr[i - 1];
    if (data === 0) break;

    for (let left = 0; left < 5; left++) {
        for (let right = 0; right < 5; right++) {
            if (dp[i - 1][left][right] === INF) continue;

            if (data !== right) {
                dp[i][data][right] = Math.min(dp[i][data][right], dp[i - 1][left][right] + calc_score(left, data));
            }
            if (data !== left) {
                dp[i][left][data] = Math.min(dp[i][left][data], dp[i - 1][left][right] + calc_score(right, data));
            }
        }
    }

    lastData = data;
}

console.log(Math.min(...dp[arr.length - 1][lastData]));
