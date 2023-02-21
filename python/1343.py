import sys

## 1
input_text = sys.stdin.readline().rstrip()

input_text = input_text.replace("XXXX", "AAAA")
input_text = input_text.replace("XX", "BB")

if ("X" in input_text):
    print(-1)
else:
    print(input_text)

### 2
input_text = sys.stdin.readline().rstrip()
A_polyomino = "AAAA"
B_polyomino = "BB"
result_polyomino = ""

if ("." in input_text):
    splited_text = input_text.split(".")

    for item in splited_text:
        if (len(item) == 0):
            result_polyomino = result_polyomino + "."
        elif (len(item) % 2 == 0):
            result_polyomino = result_polyomino + (A_polyomino * (len(item) // 4)) + (B_polyomino * (len(item) % 4 - 1)) + "."
        else:
            result_polyomino = -1
            break

    if (result_polyomino != -1):
        result_polyomino = result_polyomino[:-1]
else:
    if (len(input_text) % 2 == 0):
        result_polyomino = A_polyomino * (len(input_text) // 4) + B_polyomino * (len(input_text) % 4 - 1)
    else:
        result_polyomino = -1

print(result_polyomino)