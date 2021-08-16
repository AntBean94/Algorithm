# BOJ 10871 X보다 작은 수

N, X = map(int, input().split())
arr = list(map(int, input().split())) 
for x in arr:
    if x < X:
        print(x, end=' ') 