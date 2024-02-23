import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    num = int(input())

    if (num == 0):
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)