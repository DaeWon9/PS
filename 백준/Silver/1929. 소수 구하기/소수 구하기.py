import sys
import math

N, M = map(int,sys.stdin.readline().split())

def is_sosu(num):
    if (num == 1):
        return False
    else:  
        for i in range(2, int(math.sqrt(num)) + 1):
            if(num % i == 0):
                return False
        return True

for i in range(N, M+1):
    if (is_sosu(i)):
        print(i)