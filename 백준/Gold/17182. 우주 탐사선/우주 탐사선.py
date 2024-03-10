import sys
input = sys.stdin.readline

def solution(vertex, time, count):
    global answer
    if (N == count):
        answer = min(answer, time)
        return
    
    for v in range(N):
        if not visited[v]:
            visited[v] = True
            solution(v, time + graph[vertex][v], count + 1)
            visited[v] = False

N, K = map(int,input().split())
graph = []
visited = [False for _ in range(N)]
visited[K] = True
answer = 2147483647

for _ in range(N):
    graph.append(list(map(int, input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

solution(K, 0, 1)
print(answer)