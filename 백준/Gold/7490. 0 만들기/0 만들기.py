import sys
input = sys.stdin.readline

operators = [' ', '+', '-']

def solve(start, N, result_len, path: str = ""):
    if (len(path) == result_len and eval(path.replace(" ", "")) == 0):
        print(path)
        return
    
    for i in range(start, N+1):
        for operator in operators:
            path += operator+str(i)
            solve(i+1, N,result_len, path)
            path = path[:-2]
 
T = int(input())

for _ in range(T):
    N = int(input())
    solve(2, N, N*2-1, "1")
    print('')