# BOJ 15654 N과 M (5)

'''
순열 - 재귀
'''

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
vis = [0] * (N + 1)

def recur(arr, vis, l):
    # 길이를 만족하면 출력
    if l == M:
        print(*arr)
        return
    # 원소 추가
    for i in range(N):
        n = nums[i]
        # 중복하는 경우 제외
        if not vis[i]:
            arr.append(n)
            vis[i] = 1
            recur(arr, vis, l + 1)
            arr.pop()
            vis[i] = 0

recur([], vis, 0)