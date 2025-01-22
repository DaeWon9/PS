import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
answer = set()

if (N == 1):
    print('A')
    exit(0)

pivot_a = arr[0]
pivot_b = arr[1]

for a in range(-200, 200):
    b = pivot_b - pivot_a * a
    flag = True
    for i in range(1, N-1):
        aa = arr[i]
        bb = arr[i+1]

        if (aa * a + b != bb):
            flag = False
            break
    
    if (flag):
        answer.add(arr[N-1] * a + b)

if (len(answer) == 0):
    print('B')
elif (len(answer) > 1):
    print('A')
else:
    print(*answer)