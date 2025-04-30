import sys
from collections import deque, defaultdict
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K, M, P = map(int, input().split())

    adj_vertices = defaultdict(list)
    indegree = defaultdict(int)
    outdegree = defaultdict(int)
    strahlers = [[0, 0] for _ in range(M+1)]
    queue = deque()

    goal = 0

    for _ in range(P):
        u, v = map(int, input().split()) # u -> v
        
        adj_vertices[u].append(v)
        indegree[v] += 1
        outdegree[u] += 1

    for id in range(1, M+1):
        if (outdegree[id] == 0):
            goal = id
        if (indegree[id] == 0):
            strahlers[id] = [1, 1]
            queue.append(id)

    while queue:
        v = queue.popleft()

        target_strahler = strahlers[v][0]

        if (strahlers[v][1] > 1):
            target_strahler += 1

        for adj_vertex in adj_vertices[v]:
            indegree[adj_vertex] -= 1
            if (strahlers[adj_vertex][0] == 0):
                strahlers[adj_vertex] = [target_strahler, 1]
            elif (strahlers[adj_vertex][0] == target_strahler):
                strahlers[adj_vertex][1] += 1
            elif (strahlers[adj_vertex][0] < target_strahler): # big
                strahlers[adj_vertex] = [target_strahler, 1]
            
            if (indegree[adj_vertex] == 0):
                queue.append(adj_vertex)

    answer = strahlers[goal][0]
    if (strahlers[goal][1] > 1):
        answer += 1

    print(K, answer)