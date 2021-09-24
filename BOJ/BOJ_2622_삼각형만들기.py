# BOJ 2622 삼각형만들기

'''
a에 따라 가능한 b의 갯수만 결정하면 됨

1. a 범위
1 <= a <= L // 3

2. b 범위
max(a, (L-2a)/2) <= b <= (L-a)/2
'''

N = int(input())
cnt = 0
for a in range(1, N // 3 + 1):
    cnt += ((N-a)//2+1) - max(a, (N-2*a)//2+1)
print(cnt)