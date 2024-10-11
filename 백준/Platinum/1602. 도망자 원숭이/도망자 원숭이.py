from sys import stdin, maxsize
input = stdin.readline

# Q개의 질문에서 S, T 가 달리지는데, 이에 모든 경로의 최단경로를 한 번에 구해야함
# 플로이드 워셜
# 인덱스는 1부터 시작
# 멍멍이에 대한 정보도 따로 관리

N, M, Q = map(int, input().split())

dog_input = [0] + list(map(int, input().split()))
dog_time = []
for i, value in enumerate(dog_input):
    dog_time.append((value, i))
dog_time.sort()

dog_graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
distance_graph = [[maxsize for _ in range(N + 1)] for _ in range(N + 1)]
path = [[[r] for _ in range(N + 1)] for r in range(N + 1)]
questions = []

for _ in range(M):
    v1, v2, time = map(int, input().split())
    dog = max(dog_input[v1], dog_input[v2])
    distance_graph[v1][v2] = time
    distance_graph[v2][v1] = time
    dog_graph[v1][v2] = dog
    dog_graph[v2][v1] = dog

for _ in range(Q):
    questions.append(tuple(map(int, input().split())))

for dog, k in dog_time:
    if (k == 0):
        continue

    distance_graph[k][k] = 0
    dog_graph[k][k] = dog

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dog_value = max(dog_graph[i][k], dog_graph[k][j])
            distance_value = distance_graph[i][k] + distance_graph[k][j]
            if (distance_graph[i][j] + dog_graph[i][j] > distance_value + dog_value):
                distance_graph[i][j] = distance_value
                dog_graph[i][j] = dog_value

for S, T in questions:
    if (distance_graph[S][T] == maxsize):
        print(-1)
    else:
        print(distance_graph[S][T] + dog_graph[S][T])