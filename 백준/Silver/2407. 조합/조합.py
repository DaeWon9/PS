import math
from fractions import Fraction

n, m = map(int, input().split(" "))

if (n-m < m):
    m = n-m

print(Fraction(math.factorial(n), (math.factorial(m) * math.factorial(n-m))))