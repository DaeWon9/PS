import sys
import heapq

n = int(sys.stdin.readline())
heap = []
result = 0

for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))

for _ in range(n - 1):
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    result += num1 + num2

    heapq.heappush(heap, num1 + num2)

print(result)
