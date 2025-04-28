import sys
input = sys.stdin.readline

# 엘자의 눈사람의 키를 고정하고
# 안나의 눈사람 탐색

N = int(input()) # 4 ≤ N ≤ 600
H = list(map(int, input().split()))
H.sort()

answer = float('inf')

for i in range(N - 1):
    for j in range(N - 1, i, -1):
        elsa_snowman_h = H[i] + H[j]

        left = i+1
        right = j-1
        
        while left < right:
            anna_snowman_h = H[left] + H[right]
            diff = abs(elsa_snowman_h - anna_snowman_h)
            answer = min(answer, diff)

            if (anna_snowman_h == elsa_snowman_h): # 아예 같다면 바로 종료
                print(0)
                exit(0)
            elif (anna_snowman_h < elsa_snowman_h): # 안나의 눈사람을 더 키워야함.
                left += 1
            else:
                right -= 1

print(answer)