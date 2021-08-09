# BOJ 15683 감시

'''풀이
경우의 수
1: 4
2: 2
3: 4
4: 4
5: 1

번호 리스트(큐)

함수 설정 
dfs()
if k==len(cctv):
    if  set(추가된 갯수) > 최댓값:
        최댓값 = set(추가된 갯수)
    return

    tv = cctv[k]
    y = tv[0]
    x = tv[1]
    방향 경우의 수
    for i in range(dirs[tv[2]])
        해당하는 항목 탐색
        추가된 갯수 = 0
        for j in sch[i]:
            d = (i + j) % 4
            ### 함수 ###
            (추가된 갯수, 스택)
        재귀 함수 호출(dfs)
        스택에서 추가된 갯수만큼 제거
        
    
    
cnt 몇개 추가되었는지
queue 추가된 항목 담기



[a, b, c]

0. 깊이는 cctv 갯수만큼
1. 하나 뽑아서 for문(경우의수)
2. 



'''
def find_el(d, y, x, point, stack):
    while True:
        y += dy[d]
        x += dx[d]
        if 0 <= y < N and 0 <= x < M:
            if office[y][x] == 0:
                point += 1
                stack.append((y, x))
            elif office[y][x] > 5:
                break
        else:
            break
    return point

def delete_el(stack, point):
    for i in range(point):
        stack.pop()

def dfs(stack, r):
    global ans
    # 종료 조건
    if r == len(cctv):
        if len(set(stack)) > ans:
            ans = len(set(stack))
        return
    
    tv = cctv[r]
    y = tv[0]
    x = tv[1]
    for i in range(dirs[tv[2]]):
        point = 0
        for j in sch[tv[2]]:
            d = (i + j) % 4
            point = find_el(d, y, x, point, stack)
        dfs(stack, r + 1)
        delete_el(stack, point) 

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

# 상, 우, 하, 좌 (시계방향)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
dirs = [0, 4, 2, 4, 4, 1]
sch = [[0], [0], [0, 2], [0, 1], [0, 1, 2], [0, 1, 2, 3]]

pt = 0
# CCTV 정보 입력
cctv = []
for i in range(N):
    for j in range(M):
        loc = office[i][j]
        if 0 < loc < 6:
            cctv.append([i, j, loc])
        if loc != 0:
            pt += 1

# cctv별로 순회
ans = 0
stack = []
            
dfs(stack, 0)
print(N * M - (ans + pt))