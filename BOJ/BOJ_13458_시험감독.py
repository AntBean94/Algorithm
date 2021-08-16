# BOJ 13458 시험 감독
import sys
input = sys.stdin.readline

N = int(input())
supervisor = 0
applicants = list(map(int, input().split()))
first, second = map(int, input().split())
for i in applicants:
    applicant = i
    supervisor += 1
    applicant -= first
    if applicant > 0:
        supervisor += applicant // second
        if applicant % second:
            supervisor += 1
print(supervisor)
