import sys
input = sys.stdin.readline

N, L, W, H = map(float, input().split())
start = 0
end = max(L, W, H)

# A가 있다면 총 개수는 (L // A) * (W // A) * (H // A) 
# 이고 N개가 넘어야함
# (L // A) * (W // A) * (H // A)  >= N

for _ in range(100):
    mid = (start + end) / 2
    count = (L // mid) * (W // mid) * (H // mid)

    if (count >= N):
        start = mid
    else:
        end = mid

print("{:0.10f}".format(end))
