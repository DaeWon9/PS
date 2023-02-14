import sys

N, M = map(int, input().split(" "))

password_dict = dict()

for _ in range(N):
    input_data = sys.stdin.readline().rstrip().split(" ")
    password_dict[input_data[0]] = input_data[1]
    
for _ in range(M):
    input_url = sys.stdin.readline().rstrip()
    print(password_dict[input_url])
