def ccw(a, b, c):
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3- x1)

def is_intersect(a, b, c, d):
    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)

    if (ab == 0 and cd == 0): # 일직선
        if (a > b):
            a, b = b, a
        if (c > d):
            c, d = d, c
        return c < b and a < d  # 완전히 겹치면 False

    # 한 점에서만 접하는 경우 예외 처리
    if (ab == 0 or cd == 0):
        return False 

    return ab < 0 and cd < 0

x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
a, b, c, d = (x1, y1), (x2, y2), (x3, y3), (x4, y4)

print(1 if is_intersect(a, b, c, d) else 0)
