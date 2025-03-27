import sys
input = sys.stdin.readline

N, K, Q, M = map(int, input().split())
sleep_studentes = set(map(int, input().split()))
shot_students = list(map(int, input().split()))

status = [0, 0, 0] + [1] * N # 1이 출석이 안된 상태

for shot_student in shot_students:

    if (shot_student in sleep_studentes):
        continue

    m = 1
    while True:
        target = shot_student * m  
        
        if (target >= N + 3):
            break

        if (target in sleep_studentes):
            m += 1
            continue
        
        status[target] = 0
        m += 1

summed_stauts = [0] * (N + 3)
summed_stauts[3] = status[3]

for i in range(4, N + 3):
    summed_stauts[i] = summed_stauts[i-1] + status[i]

for _ in range(M):
    s, e = map(int, input().split())
    print(summed_stauts[e] - summed_stauts[s-1])

