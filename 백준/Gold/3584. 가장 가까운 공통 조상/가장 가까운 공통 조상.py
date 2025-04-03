import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    parent = [0 for _ in range(N+1)]

    for _ in range(N-1):
        A, B = map(int, input().split()) # A가 B의 부모
        parent[B] = A

    A, B = map(int, input().split())

    A_parent = [A]
    while (parent[A] != 0): # root 까지
        A_parent.append(parent[A])
        A = parent[A]
    
    B_parent = [B]
    while (parent[B] != 0): # root 까지
        B_parent.append(parent[B])
        B = parent[B]
    
    answer = A_parent[-1]
    min_len = min(len(A_parent), len(B_parent))        

    for i in range(-1, -(min_len + 1), -1):
        if (A_parent[i] == B_parent[i]):
            answer = A_parent[i]

    print(answer)