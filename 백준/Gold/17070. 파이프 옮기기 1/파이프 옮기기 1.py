import sys

n = int(sys.stdin.readline())
house = []
for _ in range(n):
    house.append(list(map(int, sys.stdin.readline().split())))

queue = []
queue.append((0, 1, 1))  # 끝위치 # 1:가로 2:세로 3:대각선
answer = 0

while queue:
    endX, endY, way = queue.pop()
    if endX == n-1 and endY == n-1:
        answer += 1
        continue

    if way == 1:
        if endY+1 < n:
            if house[endX][endY+1] == 0:
                queue.append((endX, endY+1, 1))
        if endX+1 < n and endY+1 < n:
            if house[endX][endY+1] == 0 and house[endX+1][endY] == 0 and house[endX+1][endY+1] == 0:
                queue.append((endX+1, endY+1, 3))
    elif way == 2:
        if endX+1 < n:
            if house[endX+1][endY] == 0:
                queue.append((endX+1, endY, 2))
        if endX+1 < n and endY+1 < n:
            if house[endX][endY+1] == 0 and house[endX+1][endY] == 0 and house[endX+1][endY+1] == 0:
                queue.append((endX+1, endY+1, 3))
    elif way == 3:
        if endY+1 < n:
            if house[endX][endY+1] == 0:
                queue.append((endX, endY+1, 1))
        if endX+1 < n:
            if house[endX+1][endY] == 0:
                queue.append((endX+1, endY, 2))
        if endX+1 < n and endY+1 < n:
            if house[endX][endY+1] == 0 and house[endX+1][endY] == 0 and house[endX+1][endY+1] == 0:
                queue.append((endX+1, endY+1, 3))

print(answer)
