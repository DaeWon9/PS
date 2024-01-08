import sys

n = int(sys.stdin.readline())

increase = 1
blocks = 1

for fence_count in range(2, n + 1):
    if (fence_count % 6 == 0): # 6의 배수일 때 증가량 1증가
        increase += 1
    
    blocks += increase

    if(fence_count % 6 == 1): # *의 경우
        blocks -= 1

print(blocks)

# 1 1 -> 1
# 2 2 -> 1
# 3 3 -> 1
# 4 4 -> 1
# 5 5 -> 1
# 6 7 -> 2 (6의 배수)
# 7 8 -> 1 (*)
# 8 10 -> 2
# 9 12 -> 2
# 10 14 -> 2
# 11 16 -> 2
# 12 19 -> 3 (6의 배수)
# 13 21 -> 2 (*)
# 14 24 -> 3
