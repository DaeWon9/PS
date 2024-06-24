import sys
from collections import deque

t = int(sys.stdin.readline())
reverse = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

for _ in range(t) :
    coin = []
    for i in range(3) :
        line = sys.stdin.readline().split()
        for l in line :
            if l == 'H' :
                coin.append(False)
            else :
                coin.append(True)
    queue = deque()
    queue.append((coin,0))
    visit = set()
    visit.add(str(coin))

    p = 0

    while queue :
        tmp,cnt = queue.popleft()

        a = 0
        for i in range(8) :
            if tmp[i]!=tmp[i+1] :
                a = 1
        if a==0 :
            print(cnt)
            p = 1
            break
        

        for re in reverse :
            x = [True for _ in range(9)]
            for i in range(9) :
                x[i] = tmp[i]
            for r in re :
                x[r] = not tmp[r]
            if str(x) not in visit :
                queue.append((x,cnt+1))
                visit.add(str(x))

    if p==0 :
        print(-1)
