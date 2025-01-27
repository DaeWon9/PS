const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "input.txt";
const input = fs.readFileSync(filePath).toString().trim().split("\n");

function differenceSet(set1, set2) {
    return new Set([...set1].filter((item) => !set2.has(item)));
}

function moveArduino(r, c) {
    let minDistance = 201;
    let result = [r, c];

    for (let i = 1; i < 10; i++) {
        const dr = r + directionY[i];
        const dc = c + directionX[i];

        const distance = calcDistance(IPos[0], IPos[1], dr, dc);

        if (minDistance > distance) {
            minDistance = distance;
            result = [dr, dc];
        }
    }
    return getIndex(result[0], result[1]);
}

function calcDistance(r1, c1, r2, c2) {
    return Math.abs(r1 - r2) + Math.abs(c1 - c2);
}

function getIndex(r, c) {
    return r * C + c;
}

function getPos(index) {
    return [Math.floor(index / C), index % C];
}

let [R, C] = input[0].split(" ").map(Number);
let idx = 1;
let IPos = [];
const directionX = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1];
const directionY = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1];
let arduinoPosSet = new Set();

for (let r = 0; r < R; r++) {
    inputData = input[idx++].trim();

    for (let c = 0; c < C; c++) {
        if (inputData[c] === "I") {
            IPos = [r, c];
        } else if (inputData[c] === "R") {
            arduinoPosSet.add(getIndex(r, c));
        }
    }
}

const moveDirections = input[idx++].split("").map(Number);
for (let cnt = 0; cnt < moveDirections.length; cnt++) {
    const newArduinoPosSet = new Set();
    const duplicatedPosSet = new Set();

    IPos[0] = IPos[0] + directionY[moveDirections[cnt]];
    IPos[1] = IPos[1] + directionX[moveDirections[cnt]];
    const IPosIndex = getIndex(IPos[0], IPos[1]);

    for (const idx of arduinoPosSet) {
        const arduinoPos = getPos(idx);
        const movedPosIndex = moveArduino(arduinoPos[0], arduinoPos[1]);

        if (IPosIndex === movedPosIndex) {
            console.log("kraj", cnt + 1);
            process.exit();
        }

        if (newArduinoPosSet.has(movedPosIndex)) {
            duplicatedPosSet.add(movedPosIndex);
        } else {
            newArduinoPosSet.add(movedPosIndex);
        }
    }

    arduinoPosSet = differenceSet(newArduinoPosSet, duplicatedPosSet);
}

let answer = Array.from({ length: R }, () => Array.from({ length: C }, () => "."));
answer[IPos[0]][IPos[1]] = "I";

for (const idx of arduinoPosSet) {
    const arduinoPos = getPos(idx);
    answer[arduinoPos[0]][arduinoPos[1]] = "R";
}

for (const ans of answer) {
    console.log(ans.join(""));
}
