import sys

score = dict()

for index in range(1, 9):
    score[index] = int(sys.stdin.readline())

sorted_score = sorted(score.items(), key=lambda x: x[1])
sorted_score = sorted_score[3:]
sorted_score.sort()

sum = 0

for item in sorted_score:
    sum += item[1]

print(sum)

for item in sorted_score:
    print(item[0], end=" ")