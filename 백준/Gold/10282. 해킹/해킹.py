import sys
import heapq
input = sys.stdin.readline

T = int(input())
group_sum_time = []

for _ in range(T):
    n, d, c = map(int, input().split())

    heap = [(0, c)]
    distance = [float("inf")] * (n+1)
    graph = [[] for _ in range(n+1)]
    distance[c] = 0

    for _ in range(d):
        a, b, s = map(int, input().split())

        graph[b].append((a, s))

    while heap:
        t, v = heapq.heappop(heap)

        if (distance[v] < t):
            continue

        for adj_vertex, s in graph[v]:
            new_value = t + s

            if (distance[adj_vertex] > new_value):
                distance[adj_vertex] = new_value
                heapq.heappush(heap, (new_value, adj_vertex))

    cnt = 0
    max_time = 0

    for i in range(1, n+1):
        if (distance[i] == float("inf")):
            continue

        if (max_time < distance[i]):
            max_time = distance[i]

        cnt += 1

    print(cnt, max_time)