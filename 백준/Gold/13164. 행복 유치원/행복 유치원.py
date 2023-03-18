import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
student_height_list = list(map(int, sys.stdin.readline().rstrip().split()))
height_difference_list = []

for i in range(1,N): #인접한 아이들의 키 차이
    height_difference_list.append(student_height_list[i] - student_height_list[i-1])

height_difference_list = sorted(height_difference_list, reverse=True)
print(sum(height_difference_list[K-1:]))