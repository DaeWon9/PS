import math
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    R, N = map(int, sys.stdin.readline().rstrip().split(" "))
    if (N - R < N and N != R):
        R = N - R

    print(int(math.factorial(N) / (math.factorial(N-R) * math.factorial(R))))
    