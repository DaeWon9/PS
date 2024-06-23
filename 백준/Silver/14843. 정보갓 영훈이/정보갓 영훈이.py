import sys
input = sys.stdin.readline

N = int(input())
younghoon_score = 0
score_list = []

for _ in range(N):
    S, A, T, M = map(float, input().split())
    score = (S * (1 + 1 / A) * (1 + M / T)) / 4

    younghoon_score += score

score_list.append(younghoon_score)

P = int(input())
for _ in range(P):
    score = float(input())
    score_list.append(score)

score_list.sort(reverse=True)
younghoon_rank = score_list.index(younghoon_score)
younghoon_rank += 1

total_people = P + 1
threshold = total_people * 15 / 100

younghoon_name = "Younghoon"
if (younghoon_rank <= threshold):
    younghoon_name = "Younghoon \"The God\""

print(f"The total score of {younghoon_name} is {younghoon_score:.02f}.")