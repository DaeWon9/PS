import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

first_line = list(map(int, input().split()))

for num in first_line:
    heapq.heappush(heap, num)

for _ in range(N-1):
    line = list(map(int, input().split()))

    for num in line:
        if (heap[0] < num):
            heapq.heappop(heap)
            heapq.heappush(heap, num)

print(heap[0])