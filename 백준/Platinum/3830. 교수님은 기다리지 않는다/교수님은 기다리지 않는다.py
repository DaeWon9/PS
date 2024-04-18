import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(x):
    if (parent[x] == x):
        return x
    
    p = find(parent[x])
    value_list[x] += value_list[parent[x]]
    parent[x] = p

    return parent[x]

def union(x, y, w):
    px = find(x)
    py = find(y)

    if (x == y):
        return
    
    value_list[py] = value_list[x] - value_list[y] + w 
    parent[py] = px

while True:
    N, M = map(int, input().split())

    if (N == 0 and M == 0):
        break

    parent = [i for i in range(N + 1)]
    value_list = [0 for _ in range(N + 1)]

    for _ in range(M):
        input_data = list(map(str, input().rstrip().split()))

        if (input_data[0] == '!'):
            v1, v2, w = map(int, input_data[1:])

            if (find(v1) != find(v2)):
                union(v1, v2, w)

        else: # ?
            v1, v2 = map(int, input_data[1:])

            if (find(v1) != find(v2)):
                print("UNKNOWN")
                continue
            
            print(value_list[v2] - value_list[v1])