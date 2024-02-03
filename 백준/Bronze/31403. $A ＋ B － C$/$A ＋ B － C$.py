import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

result_1 = A + B - C
result_2 = int(str(A) + str(B)) - C

print(result_1)
print(result_2)