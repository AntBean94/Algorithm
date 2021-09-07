# BOJ 1450 냅색문제

'''
Meet in the middle

1. 집합을 두 집합으로 나눈다.
2. 각 집합의 가능한 합(key)과 갯수(value)를 구한다.(해시 이용)
3. 구해진 합들의 집합을 A, B로 명명
- B를 정렬하고 value에 대한 prefix sum을 구한다.
4. A를 탐색하며B에서 A의 원소와 B의 원소가 C(최대 담을 수 있는 값)가
    되는 값을 찾는다.(이분탐색)
5. prefix sum에서 해당 key가 이분탐색으로 찾아진 값인 원소를 찾아 
    value를 더한다.
'''

import bisect
N, C = map(int, input().split())
arr = list(map(int, input().split()))

def make_group(sub_arr):
    lth = len(sub_arr)
    result = [{} for _ in range(lth + 1)]
    result[0] = {0: 1}
    for i in range(lth):
        a = sub_arr[i]
        for b in result[i].keys():
            if b in result[i+1]: result[i+1][b] += result[i][b]
            else: result[i+1][b] = result[i][b]
            if a + b in result[i+1]: result[i+1][a+b] += result[i][b]
            else: result[i+1][a+b] = result[i][b]
    return result[lth]

A = make_group(arr[:N//2])
B = make_group(arr[N//2:])
B = dict(sorted(B.items(), key=lambda item: item[0]))

# prefix sum 구하기
B_sum = {}
tmp = 0
idx = []
for key, value in B.items():
    tmp += value
    B_sum[key] = tmp
    idx.append(key)

ans = 0
# A를 순회하며 B에서 합이 C가 되는 원소를 찾는다.(해싱)
for key, value in A.items():
    b = C - key
    if b < 0: continue
    # 해당 값의 키값을 prefix sum에서 찾아 결과에 더한다.
    if b in B: ans += B_sum[b] * value
    else:
        b_idx = bisect.bisect_left(idx, b)
        b_idx = idx[b_idx - 1]
        ans += B_sum[b_idx] * value

print(ans)