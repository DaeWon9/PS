import sys
from collections import deque, defaultdict

def soluton(adjoint_vertecies, v):
    queue = deque()
    visited = [False for _ in range(v + 1)]
    group_flag = [False for _ in range(v + 1)]
    vertex_list = adjoint_vertecies.keys()
    start_group_flag = True

    for vertex in vertex_list:
        if (visited[vertex]):
            continue

        queue.append((start_group_flag, vertex))
        group_flag[vertex] = start_group_flag
        visited[vertex] = True

        while(queue):
            flag, v = queue.popleft()
            for adjoint_vertex in adjoint_vertecies[v]:
                if (not visited[adjoint_vertex]): 
                    queue.append((not flag, adjoint_vertex))
                    group_flag[adjoint_vertex] = not flag
                    visited[adjoint_vertex] = True 
                    continue
                if (visited[adjoint_vertex] and group_flag[adjoint_vertex] == flag):
                    print("NO")
                    return
    print("YES")
    return

input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    v, e = map(int, input().split())
    adjoint_vertecies = defaultdict(list)
    
    for _ in range(e):
        v1, v2 = map(int, input().split())
        adjoint_vertecies[v1].append(v2)
        adjoint_vertecies[v2].append(v1)

    soluton(adjoint_vertecies, v)