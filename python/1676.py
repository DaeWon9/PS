import math

N = int(input())

zero_count = 0

factorial = math.factorial(N)

while(factorial > 9):
    if factorial % 10 == 0:
        zero_count = zero_count + 1
    else:
        break

    factorial = factorial // 10

print(zero_count)