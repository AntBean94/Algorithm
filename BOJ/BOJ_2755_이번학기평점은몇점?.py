# BOJ 2755 이번학기 평점은 몇점?

score = {
    "A+": 4.3, "A0": 4.0, "A-": 3.7,
    "B+": 3.3, "B0": 3.0, "B-": 2.7,
    "C+": 2.3, "C0": 2.0, "C-": 1.7,
    "D+": 1.3, "D0": 1.0, "D-": 0.7,
    "F": 0
}

total = 0
credits = 0
N = int(input())
for i in range(N):
    subject, point, grade = input().split()
    total += int(point) * score[grade]
    credits += int(point)

ans = round(total / credits + 0.00000000001, 2)
print(format(ans, ".2f"))