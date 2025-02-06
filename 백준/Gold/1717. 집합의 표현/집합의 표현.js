const fs = require("fs");
const input = fs.readFileSync(0, 'utf-8').toString().trim().split("\n");

const find = (x) => {
    if (x === parent[x]) {
        return x;
    }

    parent[x] = find(parent[x]);
    return parent[x];
};

const union = (x, y) => {
    x = find(x);
    y = find(y);

    if (x === y) return;

    if (x < y) {
        parent[y] = x;
    } else {
        parent[x] = y;
    }
};

const [N, M] = input[0].split(" ").map(Number);
let idx = 1;
let parent = Array.from({ length: N + 1 }, (_, i) => i);

for (let i = 0; i < M; i++) {
    const [t, a, b] = input[idx++].split(" ").map(Number);
    if (t === 0) {
        union(a, b);
    } else {
        if (find(a) === find(b)) console.log("YES");
        else console.log("NO");
    }
}
