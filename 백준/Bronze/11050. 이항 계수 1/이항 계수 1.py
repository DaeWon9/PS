import sys
from math import comb
input = sys.stdin.readline

N, K = map(int, input().split())
print(comb(N, K))