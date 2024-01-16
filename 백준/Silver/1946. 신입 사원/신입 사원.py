import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    answer = 1
    
    rank_list = []

    for id in range(N):
        rank1, rank2 = map(int, sys.stdin.readline().split())
        rank_list.append((rank1, rank2))

    rank_list.sort(key=lambda x : x[0])

    min_rank2 = rank_list[0][1]

    for index in range(1, N):
        is_possible = True

        if (min_rank2 > rank_list[index][1]):
            min_rank2 = rank_list[index][1]
            answer += 1

    print(answer)