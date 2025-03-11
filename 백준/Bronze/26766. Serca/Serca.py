import sys
input = sys.stdin.readline

def print_heart():
    print(" @@@   @@@ ")
    print("@   @ @   @")
    print("@    @    @")
    print("@         @")
    print(" @       @ ")
    print("  @     @  ")
    print("   @   @   ")
    print("    @ @    ")
    print("     @     ")

n = int(input())

for _ in range(n):
    print_heart()