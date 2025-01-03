import sys
input = sys.stdin.readline

target = input().rstrip()
target_len = len(target)
N = int(input())
answer = 0

for _ in range(N):
    input_data = input().rstrip()
    input_data = input_data + input_data[:target_len]

    if (target in input_data):
        answer += 1

print(answer)