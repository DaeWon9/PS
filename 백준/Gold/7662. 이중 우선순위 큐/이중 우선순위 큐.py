import sys
import heapq

t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())

    visited = [False] * k
    max_heap = []
    min_heap = []

    for key in range(k):
        process, value = map(str, sys.stdin.readline().split())

        if process == "I":
            heapq.heappush(min_heap, (int(value), key))
            heapq.heappush(max_heap, (-int(value), key))
            visited[key] = True
        else:
            if value == "1":
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not max_heap or not min_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
