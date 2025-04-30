import sys
input = sys.stdin.readline

def is_visible(buildings, i, j):
    if (i > j):
        i, j = j, i
    
    slope = (buildings[j] - buildings[i]) / (j - i)
    
    for k in range(i + 1, j):
        curr_slope = (buildings[k] - buildings[i]) / (k - i)
        if (curr_slope >= slope):
            return False
    return True

N = int(input())
buildings = list(map(int, input().split()))
max_count = 0

for i in range(N):
    count = 0
    # Left
    for j in range(i-1, -1, -1):
        if (is_visible(buildings, i, j)):
            count += 1
    # Right
    for j in range(i+1, N):
        if (is_visible(buildings, i, j)):
            count += 1

    max_count = max(max_count, count)

print(max_count)
