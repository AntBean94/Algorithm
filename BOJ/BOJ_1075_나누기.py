# BOJ 1075 나누기

N = int(input())
F = int(input())
N = 100 * (N // 100)
for i in range(100):
    nxt_N = N + i
    if not nxt_N % F:
        if i < 10:
            print(f"0{i}")
        else:
            print(i)
        break