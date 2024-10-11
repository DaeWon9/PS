import sys
input = sys.stdin.read
output = sys.stdout.write

output("50 49\n")
for i in range(49, 0, -1):
    output(f"{i} {i + 1} -1\n")