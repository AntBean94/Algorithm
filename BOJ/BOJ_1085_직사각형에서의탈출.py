# BOJ 1085 직사각형에서의 탈출

x, y, w, h = map(int, input().split())
ans = []
if 2 * x < w:
    ans.append(x)
else:
    ans.append(w-x)
if 2 * y < h:
    ans.append(y)
else:
    ans.append(h-y)
print(min(ans))