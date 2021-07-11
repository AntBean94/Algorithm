import sys

sys.stdin = open("input.txt", "r")

T = int(input())
arr = []
for t in range(T):
    arr.append(int(sys.stdin.readline()))
arr.sort()
for i in arr:
    sys.stdout.writelines(str(i) + '\n')