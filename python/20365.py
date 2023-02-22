import sys

N = int(input())
input_text = sys.stdin.readline().rstrip()

B_splited_text = input_text.split("R")
R_splited_text = input_text.split("B")
count = min(len(B_splited_text) - B_splited_text.count(""), len(R_splited_text) - R_splited_text.count(""))

print(count + 1)