const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

const solve = (v, path = []) => {
    if (path.length === 5) {
        return true;
    }

    for (const adjVertex of adjVertices[v]) {
        if (!path.includes(adjVertex)) {
            path.push(adjVertex);
            if (solve(adjVertex, path)) {
                return true;
            }
            path.pop();
        }
    }

    return false;
};

let idx = 1;
const [N, M] = input[0].split(" ").map(Number);
const adjVertices = Array.from({ length: N }, () => []);

for (let i = 0; i < M; i++) {
    const [u, v] = input[idx++].split(" ").map(Number);

    adjVertices[u].push(v);
    adjVertices[v].push(u);
}

for (let root = 0; root < N; root++) {
    if (solve(root)) {
        console.log(1);
        process.exit(0);
    }
}
console.log(0);
