import sys
import heapq
input = sys.stdin.readline

N = int(input())
time_list = []

for _ in range(N):
    time_list.append(list(map(int, input().split())))

time_list.sort()

heap = []
for start_time, finish_time in time_list:
    if not heap:
        heapq.heappush(heap, finish_time)
        continue

    if heap[0] <= start_time:
        heapq.heappop(heap)
    heapq.heappush(heap, finish_time)

print(len(heap))