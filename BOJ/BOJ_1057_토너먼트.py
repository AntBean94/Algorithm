# BOJ 1057 토너먼트

'''
내가 10번이었으면
다음에 5번
5번이었으면 다음에
3번
3번이었으면 다음에
2번

즉, 홀수라면 N / 2 + 1
짝수라면 N / 2
'''

N, Kim, Im = map(int, input().split())

def make_group(x, cnt=20):
    arr = []
    while cnt:
        if bin(x)[-1] == '0':   # 짝수라면
            arr.append(x)
            x //= 2
        else:   # 홀수라면
            arr.append(x)
            x = int(x / 2) + 1
        cnt -= 1
    return arr

kims = make_group(Kim)
ims = make_group(Im)
for i in range(20):
    if kims[i] == ims[i]:
        print(i)
        break