# BOJ 22351 수학은 체육과목 입니다 3 (대회 문제)

n = input()

loc = 0
lth = 1
start = n[loc]
while lth <= (1/2) * len(n) and loc + lth < len(n):
    num = int(n[loc:loc+lth])
    nxt = num + 1
    lth_n = len(str(nxt))
    if nxt == int(n[loc+lth:loc+lth+lth_n]):
        loc += lth
        lth = lth_n
    else:
        loc = 0
        lth += 1
        start = n[loc:loc+lth]
end = n[len(n)-lth:]
if lth > 1/2 * len(n):
    if int(start)+1 != int(end):
        start = n
        end = n
print(start, end)