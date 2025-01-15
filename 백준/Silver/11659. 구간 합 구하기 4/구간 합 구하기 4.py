import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
summed_arr = [0 for _ in range(N)]
summed_arr[0] = arr[0]

for i in range(1, N):
    summed_arr[i] = summed_arr[i-1] + arr[i]

for _ in range(M):
    s, e = map(int, input().split())
    answer = summed_arr[e-1]
    if (s-2 >= 0):
        answer -= summed_arr[s-2]

    print(answer)
