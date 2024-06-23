import sys
input = sys.stdin.readline

W, H = map(int, input().split())
print("{:.1f}".format(W * H / 2))