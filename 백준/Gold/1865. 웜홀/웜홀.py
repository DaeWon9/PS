import sys

case_count = int(sys.stdin.readline())

for _ in range(case_count):
    n, m, w = map(int, sys.stdin.readline().split())  
    edges = []
    distance = [0] * (n + 1)
    is_has_minus_cycle = False

    for _ in range(m):
        start, end, time = map(int, sys.stdin.readline().split())
        edges.append((start, end, time))
        edges.append((end, start, time))
    
    for _ in range(w):
        start, end, time = map(int, sys.stdin.readline().split())
        edges.append((start, end, -time))

    for count in range(n):
        for start, end, time in edges:
            if (distance[end] > distance[start] + time):
                distance[end] = distance[start] + time

                if (count == n - 1):
                    is_has_minus_cycle = True
                    break
    
    if (is_has_minus_cycle):
        print('YES')
    else:
        print('NO')