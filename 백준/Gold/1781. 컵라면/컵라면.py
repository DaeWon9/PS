import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
arr = [0] * (n + 1)

for _ in range(n):
    d, w = map(int, input().split())
    heapq.heappush(heap, (-w, -d))

next_available_day = [i for i in range(n + 1)]

def find_available_day(d):
    if next_available_day[d] != d:
        next_available_day[d] = find_available_day(next_available_day[d])
    return next_available_day[d]

while heap:
    w, d = heapq.heappop(heap)
    w, d = -w, -d

    available_day = find_available_day(d)

    if available_day == 0:
        continue

    arr[available_day] = w
    next_available_day[available_day] = available_day - 1

print(sum(arr))
