const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

/* 세 점이 일직선 위에 있는 경우는 없다. */
const ccw = (A, B, C) => {
    const [x1, y1] = A;
    const [x2, y2] = B;
    const [x3, y3] = C;

    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1);
};

const isIntersect = (A, B, C, D) => {
    const ab = ccw(A, B, C) * ccw(A, B, D);
    const cd = ccw(C, D, A) * ccw(C, D, B);

    return ab < 0 && cd < 0;
};

const L1 = input[0].split(" ").map(Number);
const L2 = input[1].split(" ").map(Number);

const A = [L1[0], L1[1]];
const B = [L1[2], L1[3]];
const C = [L2[0], L2[1]];
const D = [L2[2], L2[3]];

if (isIntersect(A, B, C, D)) {
    console.log(1);
} else {
    console.log(0);
}
