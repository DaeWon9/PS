import sys
from collections import defaultdict

n = int(sys.stdin.readline())
fibo_dict = defaultdict(int)

fibo_dict[0] = 0
fibo_dict[1] = 1

# 10^k 로 나눌때 주기는 15 x 10^(k-1)
mod = 1000000
period = 1500000

for i in range(2, period):
    fibo_dict[i] = fibo_dict[i - 1] + fibo_dict[i - 2]
    fibo_dict[i] %= mod

print(fibo_dict[n % period])