import sys
input = sys.stdin.readline

def solution(combi:list, pivot):
    if (len(combi) == M):
        print(*combi)
        return
    
    for i in range(1, N + 1):
        combi.append(num_list[i])
        solution(combi, i + 1)
        combi.pop()

N, M = map(int, input().split())
num_list = [0] + list(map(int, input().split()))
num_list.sort()

solution([], 1)