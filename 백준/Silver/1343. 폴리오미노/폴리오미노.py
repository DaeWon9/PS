import sys

input_text = sys.stdin.readline().rstrip()

input_text = input_text.replace("XXXX", "AAAA")
input_text = input_text.replace("XX", "BB")

if ("X" in input_text):
    print(-1)
else:
    print(input_text)