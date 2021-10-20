# BOJ 1259 팰린드롬수

while True:
    n = input()
    if n == '0': break
    t = len(n)
    if t % 2: l, r = t // 2, t // 2
    else: l, r = t // 2 - 1, t // 2
    check = True
    while l >= 0 and r < t:
        if n[l] != n[r]:
            print('no')
            check = False
            break
        l -= 1
        r += 1
    if check: print('yes')