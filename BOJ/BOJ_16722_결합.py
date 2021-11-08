# BOJ 16722 결합

'''
세개의 집합을 합집합 했을때 원소의 갯수가 9개이면 통과

9개 중에 3개
3*4*7 = 94
'''

from itertools import combinations as cb
# card info
C = 9
cards = [list(input().split()) for _ in range(C)]
N = int(input())
cmds = [list(input().split()) for _ in range(N)]
check = {}
score, cnt, pos = 0, 0, True

for case in cb([i for i in range(9)], 3):
    id = "".join(map(str, case))
    a, b, c = case
    shape = len(set([cards[a][0], cards[b][0], cards[c][0]]))
    color = len(set([cards[a][1], cards[b][1], cards[c][1]]))
    background = len(set([cards[a][2], cards[b][2], cards[c][2]]))
    if (shape == 1 or shape == 3) and (color == 1 or color == 3) and (background == 1 or background == 3):
        check[id] = 1
        cnt += 1

for cmd in cmds:
    if cmd[0] == "H":
        a, b, c = map(int, cmd[1:])
        id = "".join(map(str, sorted([a - 1, b - 1, c - 1])))
        if id in check and check[id]:
            score += 1
            cnt -= 1
            check[id] -= 1
        else: score -= 1
    else:
        if not cnt and pos:
            score += 3
            pos = False
        else:
            score -= 1

print(score)