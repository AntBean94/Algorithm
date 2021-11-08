# BOJ 1283 단축키 지정

N = int(input())
opt = [list(input().split()) for _ in range(N)]
alpha = "abcdefghijklmnopqrstuvwxyz"
check = {i: 0 for i in alpha}
for i in range(N):
    l = len(opt[i])
    prog = True
    # 1. 첫번째 알파벳
    for j in range(l):
        word = opt[i][j]
        char = word[0].lower()
        if not check[char]:
            check[char] = 1
            opt[i][j] = f"[{word[0]}]{word[1:]}"
            prog = False
            break
    if not prog: continue
    # 2. 모든 알파벳
    for j in range(l):
        word = opt[i][j]
        for k in range(len(word)):
            char = word[k].lower()
            if not check[char]:
                check[char] = 1
                opt[i][j] = f"{word[:k]}[{word[k]}]{word[k+1:]}"
                prog = False
                break
        if not prog: break
for o in opt:
    print(" ".join(o))