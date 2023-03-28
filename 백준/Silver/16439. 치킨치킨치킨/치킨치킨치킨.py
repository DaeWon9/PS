import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().rstrip().split())
like_list = []

for _ in range(N):
    like_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

maxSum = 0
for a, b, c in combinations(range(M), 3):
    temp = 0
    for i in range(N):
        temp += max(like_list[i][a], like_list[i][b], like_list[i][c])
    maxSum = max(maxSum, temp)

print(maxSum)