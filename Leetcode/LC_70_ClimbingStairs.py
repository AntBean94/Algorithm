
'''
n개의 계단을 올라야한다.

한번에 한개 또는 두개의 계단을 오를 수 있다.


상황

데이터 A, B, C

AA, BB, CC


n개의 계단이 주어졌을 때
1, 2개씩 올라갈 수 있는 상황에서
끝까지 올라갈 수 있는 몇개의 경우의 수가 존재하는가?

[]

n0 n1 n2 n3 n4
0 1 2 3 5 8 13 .....

1 1 1
2 1

1 2

An = An-1 + An-2

3개


[0, 0, 0, 0, 0, 0, 0, ...]

n = 45

재귀함수
def function(n, n-1):
    return function(n-1, n-2) + function()


'''


class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0] * 50
        arr[1], arr[2] = 1, 2
        for i in range(3, n + 1):
            arr[i] = arr[i-1] + arr[i-2]
        print(arr[n])

func = Solution.climbStairs([], 45)
