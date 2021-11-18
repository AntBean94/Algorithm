# LeetCode 1267 Count Servers that Communicate

grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]

H = len(grid)
W = len(grid[0])
row = [0] * H
col = [0] * W
for i in range(H):
    for j in range(W):
        if grid[i][j]:
            row[i] += 1
            col[j] += 1

result = 0
for i in range(H):
    for j in range(W):
        if grid[i][j]:
            val = row[i] + col[j]
            if val > 2:
                result += 1
print(result)