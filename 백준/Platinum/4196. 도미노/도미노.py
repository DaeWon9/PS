import sys
from collections import defaultdict, deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    adj_vertices = defaultdict(list)
    indegree = defaultdict(int)
    outdegree = defaultdict(int)
    remain_domino = set(i for i in range(1, N+1))
    visited = [False] * (N + 1)

    queue = deque()
    answer = 0

    for _ in range(M):
        x, y = map(int, input().split()) # x번 블록이 넘어지면 y번 블록도 넘어짐

        indegree[y] += 1
        outdegree[x] += 1
        adj_vertices[x].append(y)

    for idx in range(1, N+1):
        if (indegree[idx] == 0):
            queue.append(idx)
            answer += 1
            remain_domino.remove(idx)

    while queue:
        v = queue.popleft()

        for adj_vertex in adj_vertices[v]:
            if (visited[adj_vertex]):
                continue
            
            queue.append(adj_vertex)
            if (adj_vertex in remain_domino):
                remain_domino.remove(adj_vertex)
                visited[adj_vertex] = True

    while remain_domino:
        max_outdegree = 0
        target_domino = 0
        for key in remain_domino:
            if (outdegree[key] > 0 and max_outdegree < outdegree[key]):
                target_domino = key
                max_outdegree = outdegree[key]

        remain_domino.remove(target_domino)
        queue.append(target_domino)
        answer += 1
        visited[target_domino] = True

        while queue:
            v = queue.popleft()

            for adj_vertex in adj_vertices[v]:
                if (visited[adj_vertex]):
                    continue
                
                queue.append(adj_vertex)
                if (adj_vertex in remain_domino):
                    remain_domino.remove(adj_vertex)
                    visited[adj_vertex] = True

    print(answer)