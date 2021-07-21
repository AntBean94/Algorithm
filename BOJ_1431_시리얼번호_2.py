import sys

def digit_sum(num):
    return sum(int(c) for c in num if c.isdigit())

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(sys.stdin.readline())
numbers.sort()
numbers.sort(key=digit_sum)
numbers.sort(key=len)
sys.stdout.write("".join(numbers))