import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

flag = True

for i in range(N-1):
    if (A[i] < A[i+1]):
        if not flag:
            print("NO")
            exit(0)
    elif (A[i] > A[i+1]):
        flag = False
    else:
        print("NO")
        exit(0)

print("YES")