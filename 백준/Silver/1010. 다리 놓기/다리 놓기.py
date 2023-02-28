import math

T = int(input())

for _ in range(T):
    R, N = map(int, input().split(" "))
    if (N - R < N and N != R):
        R = N - R

    print(int(math.factorial(N) / (math.factorial(N-R) * math.factorial(R))))