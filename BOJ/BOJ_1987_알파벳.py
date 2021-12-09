# BOJ 1987 알파벳

'''
백트래킹
'''

R, C = map(int, input().split())
board = [list() for _ in range(R)]
for i in range(R):
    tmp = input()
    for j in range(C):
        board[i].append(tmp[j])
vis = [0] * 100
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x, r):
    if r == 26:
        print(26)
        exit()
    result = r
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < R and 0 <= nx < C:
            char = board[ny][nx]
            if not vis[ord(char)]:
                vis[ord(char)] = 1
                result = max(result, dfs(ny, nx, r + 1))
                vis[ord(char)] = 0
    return result

vis[ord(board[0][0])] = 1
print(dfs(0, 0, 1))