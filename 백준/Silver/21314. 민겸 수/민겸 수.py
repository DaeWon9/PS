import sys

input_string = sys.stdin.readline().rstrip()
max_string = ""
temp = 0
if ("K" in input_string):
    for index in range(len(input_string)):
        if (input_string[index] == "K"):
            max_string = max_string + ("5" + ("0" * (index - temp)))
            temp = index + 1
        
        if (index == len(input_string) - 1 and input_string[index] == "M"):
            max_string = max_string + ("1" * (index - temp + 1))

    print(max_string)
    print(input_string.replace("K", "5").replace("M", "1").replace("11", "10").replace("01","00"))
else:
    print("1" * len(input_string)) # max 
    print("1" + ("0" * (len(input_string) - 1))) # min