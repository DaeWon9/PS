import sys
input = sys.stdin.readline

# “type c" : 현재 글의 가장 뒤에 문자 c를 추가한다.
# “undo t" : 이전 t초동안 수행된 작업을 역순으로 되돌린다.

# 항상 시간이 오름차순으로 주어진다.

N = int(input())
stack = [('', 0)]

for _ in range(N):
    p, c, t = map(str, input().split())
    t = int(t)

    if (p == 'type'):
        prev = stack[-1][0]
        stack.append((prev + c, t))
    else: # undo
        target_time = max(0, t - int(c) - 1)

        for idx in range(len(stack)-1, -1, -1):
            if (stack[idx][1] <= target_time):
                stack.append((stack[idx][0], t))
                break

print(stack[-1][0])