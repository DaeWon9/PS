import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
wire_list = [[0, 0] for _ in range(N)]
switch_dict = dict()

for idx, switch in enumerate(list(map(int, input().split()))):
    wire_list[idx][0] = switch
    switch_dict[switch] = idx

for idx, bulb in enumerate(list(map(int, input().split()))):
    wire_list[switch_dict[bulb]][1] = idx

# 전구의 value -> LIS 찾기
LIS = [wire_list[0][1]] # init
memo = [(0, wire_list[0][0])]

for i in range(1, N):
    if (wire_list[i][1] > LIS[-1]):
        LIS.append(wire_list[i][1])
        memo.append((len(LIS) - 1, wire_list[i][0]))
    else:
        idx = bisect_left(LIS, wire_list[i][1])
        LIS[idx] = wire_list[i][1]
        memo.append((idx, wire_list[i][0]))

answer = []
last_idx = len(LIS) - 1
for i in range(len(memo)-1, -1, -1):
    if (memo[i][0] == last_idx):
        answer.append(memo[i][1])
        last_idx -= 1

answer.sort()
print(len(LIS))
print(*answer)