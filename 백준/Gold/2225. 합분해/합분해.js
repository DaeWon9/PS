const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const [N, K] = input[0].split(" ").map(Number);

const dp = Array.from({ length: N + 1 }, () => Array.from({ length: K + 1 }, () => 0));
dp[0] = Array(K + 1).fill(1);
dp[0][0] = 0;

for (let n = 1; n <= N; n++) {
    for (let k = 1; k <= K; k++) {
        dp[n][k] = (dp[n - 1][k] + dp[n][k - 1]) % 1000000000;
    }
}

console.log(dp[N][K]);
