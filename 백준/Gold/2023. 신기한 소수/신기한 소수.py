import sys
input = sys.stdin.readline

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def combination(path: list = [], result: list = []):
    if (len(path) == N):
        result.append(int(''.join(map(str, path))))
        return
    
    for i in range(1, 10):
        path.append(i)
        curNum = int(''.join(map(str, path)))

        if (is_prime(curNum)):
            combination(path, result)
            
        path.pop()

    return result

N = int(input())
for result in combination():
    print(result)
