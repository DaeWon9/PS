import sys
input = sys.stdin.readline

def solve(s):
    if (not s):
        return
        
    if (s == S):
        print(1)
        exit(0)
    
    if (s[-1] == 'A'):
        solve(s[:-1])
    
    if (s[0] == 'B'):
        solve(s[1:][::-1])

# S -> T 가능??
# 문자열의 뒤에 A를 추가한다.
# 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.

# 역으로 생각해보자
# T -> S 가 가능한지 보는거.
# 문자열의 뒤에 A를 제거한다.
# 문자열을 뒤집는다. 문자열의 뒤에 B를 제거한다. == 문자열의 앞에 B를 제거하고 문자열을 뒤집는다.

S = input().rstrip()
T = input().rstrip()

solve(T)
print(0)
