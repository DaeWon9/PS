import sys
import math
input = sys.stdin.readline

X, Y, PX, PY = map(int, input().split())
max_pos = math.lcm(X, Y) + max(PX, PY)
flag = False

while (PX <= max_pos and PY <= max_pos):
    if (PX < PY):
        PX += X
    elif (PY < PX):
        PY += Y
    else:
        flag = True
        break

print(PX if flag else -1)