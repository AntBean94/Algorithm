# BOJ 2847 게임을 만든 동준이

# 배열에 넣고 뒤에서부터 1씩 빼면서 더 크면 그만큼의 차이를 적립하는 식으로 풀이
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
ans = 0
pre = 20000
for i in arr[::-1]:
    # 크거나 같으면
    if i > pre:
        ans += i - pre
        pre -= 1
    # 작으면
    else:
        pre = i - 1
print(ans)

