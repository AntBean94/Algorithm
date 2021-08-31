# BOJ 1300 K번째 수

'''
전체 배열에서 어떤 수 M보다 작거나 같은 수의 갯수는
그 수보다 한단계 큰 수의 인덱스를 의미한다.

따라서 전체 범위를 기준으로 이분탐색을 통해 범위를 좁혀나가며
자신보다 작거나 같은 수의 갯수가 K보다 크거나 같다면 기준값(m)을 중심으로
좌측을, 아니라면 우측을 탐색해나간다.
start == end (마지막까지 확인)조건에서 출력 후 return
'''

N = int(input())
K = int(input())

# 자신보다 작은 수의 개수를 체크하는 함수
def small_cnt(k):
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(k // i, N)
    return cnt

# 이분 탐색
def binary(s, e):
    if s == e:
        print(s)
        return 
    m = (s + e) // 2
    if small_cnt(m) >= K:
        binary(s, m)
    else:
        binary(m + 1, e)

binary(1, N * N)