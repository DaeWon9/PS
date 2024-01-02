import sys
from collections import deque

def operator_1(screen_count): # 화면에 있는 이모티콘을 클립보드로 복사
    return [screen_count, screen_count]

def operator_2(screen_count, clipboard_count): # 클립보드에 있는 이모티콘을 화면에 붙여넣기
    return [screen_count + clipboard_count, clipboard_count]

def operator_3(screen_count, clipboard_count): # 화면에 있는 이모티콘 중 하나를 삭제
    return [screen_count - 1, clipboard_count]

def isPossible(screen_count, clipboard_count):
    if (0 <= screen_count < 1001 and 0 <= clipboard_count < 1001):
        return True
    return False

# 모든 행동은 1초 -> 가중치가 같음
# 연산은 3가지지만 변하는 값은 screen_count, clipboard_count 두개 -> 2차원으로 관리
target_count = int(sys.stdin.readline())
visited = [[False for _ in range(1001)] for _ in range(1001)]

queue = deque()
queue.appendleft((1, 0, 0)) # screen_count, clipboard_count, time

visited[1][0] = True

while queue:
    screen_count, clipboard_count, time = queue.popleft()

    # oper 1
    dsc, dcc = operator_1(screen_count)
    if (dsc == target_count):
        print(time + 1)
        break
    if (isPossible(dsc, dcc) and not visited[dsc][dcc]):
        queue.append([dsc, dcc, time + 1])
        visited[dsc][dcc] = True


    # oper 2
    dsc, dcc = operator_2(screen_count, clipboard_count)
    if (dsc == target_count):
        print(time + 1)
        break
    if (isPossible(dsc, dcc) and not visited[dsc][dcc]):
        queue.append([dsc, dcc, time + 1])
        visited[dsc][dcc] = True


    # oper 3
    dsc, dcc = operator_3(screen_count, clipboard_count)
    if (dsc == target_count):
        print(time + 1)
        break
    if (isPossible(dsc, dcc) and not visited[dsc][dcc]):
        queue.append([dsc, dcc, time + 1])
        visited[dsc][dcc] = True