def find(x):
    if (x == parent[x]):
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if (x == y):
        return

    if (x < y):
        parent[y] = x
    else:
        parent[x] = y
        
parent = []
def solution(n, computers):
    global parent
    parent = [i for i in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            if (computers[i][j] == 0):
                continue
                
            if (find(i) != find(j)):
                union(i, j)
    

    answer = len(set(find(i) for i in range(n)))
    
    return answer