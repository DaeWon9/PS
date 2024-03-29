import sys
input = sys.stdin.readline

def solution(combi:list, pivot):
    if (len(combi) == M):
        print(*combi)
        return
    
    for i in range(pivot, N + 1):
        combi.append(num_list[i])
        solution(combi, i)
        combi.pop()

N, M = map(int, input().split())
num_list = [i for i in range(N + 1)]

solution([], 1)