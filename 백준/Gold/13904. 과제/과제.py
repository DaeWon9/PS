import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
arr = [0] * 10001

for _ in range(n):
    d, w = map(int, input().split())
    heapq.heappush(heap, (-w, -d))

while heap:
    w, d = heapq.heappop(heap)
    w, d = -w, -d

    if (arr[d] == 0):
        arr[d] = w
        continue

    min_idx = 1
    min_w = 10001
    for i in range(d, 0, -1):
        if (min_w > arr[i]):
            min_w = arr[i]
            min_idx = i
        
        if (min_w == 0):
            break
    
    if (min_w > w):
        continue

    arr[min_idx] = w

print(sum(arr))