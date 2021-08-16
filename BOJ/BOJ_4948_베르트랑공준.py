# BOJ 4948 베르트랑 공준

num = [1] * (123456 * 2 + 1)
for i in range(2, int(len(num)**0.5)):
    if num[i]:
        n = 2
        while i * n <= len(num)-1:
            num[i * n] = 0 
            n += 1

N = True
while N:
    N = int(input())
    if not N:
        break

    cnt = 0
    for n in num[N+1:2*N+1]:
        if n:
            cnt += 1
    print(cnt)
