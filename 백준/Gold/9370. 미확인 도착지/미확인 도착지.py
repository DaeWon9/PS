import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    heap = [(0, s)]
    distance = [float('inf') for _ in range(n+1)]
    distance[s] = 0
    adj_vertices = defaultdict(list)

    for _ in range(m):
        a, b, d = map(int, input().split())
        adj_vertices[a].append((b, d))
        adj_vertices[b].append((a, d))

    goals = []
    for _ in range(t):
        goals.append(int(input()))

    while heap:
        d, v = heapq.heappop(heap)

        if (distance[v] < d):
            continue

        for vv, dd in adj_vertices[v]:
            new_dist = d + dd

            if (distance[vv] > new_dist):
                distance[vv] = new_dist
                heapq.heappush(heap, ((new_dist, vv)))

    # 그들이 급한 상황이기 때문에 목적지까지 우회하지 않고 최단거리로 갈 것이라 확신한다.
    # distance[g], distance[h]를 비교했을 때, g-h는 무조건 지났을 것이며.
    # 거리가 더 큰 정점에서 또 뻗어나가면 되지 않을까
    last_vertex = g
    defalut_dist = distance[g]
    if (distance[g] < distance[h]):
        last_vertex = h
        defalut_dist = distance[h]

    after_distance = [float('inf') for _ in range(n+1)]
    after_distance[last_vertex] = 0
    heap = [(0, last_vertex)]

    while heap:
        d, v = heapq.heappop(heap)

        if (after_distance[v] < d):
            continue

        for vv, dd in adj_vertices[v]:
            new_dist = d + dd

            if (after_distance[vv] > new_dist):
                after_distance[vv] = new_dist
                heapq.heappush(heap, ((new_dist, vv)))

    answer = []
    for goal in goals:
        if (distance[goal] == float('inf')):
            continue
        
        if (defalut_dist + after_distance[goal] == distance[goal]):
            answer.append(goal)

    answer.sort()
    print(*answer)