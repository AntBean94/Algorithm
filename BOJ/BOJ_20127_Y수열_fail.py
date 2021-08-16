# BOJ 20127 Y-수열

# 문제
'''
N개의 정수로 이루어진 수열 a1, a2,..., an이 있다.
택희는 해당 수열이 증가수열 혹은 감소수열이 되게 만들고 싶다.
증가수열은 모든 i(1 <= i < N)에 대해서 ai <= ai+1 을 만족하는 수열이고, 
감소수열은 ai >= ai+1 을 만족하는 수열이다.
택희는 해당 수열의 맨 앞의 k개의 원소를 맨 뒤로 옮겨서 증가수열 또는 감소수열을 만들고 싶다. 즉, ak+1,..., aN, a1,..., ak가 증가수열, 또는 감소수열이 돼야 한다.
옮기지 않는 경우는 k=0이라고 하자. 이때, 적절한 k를 골라서 원하는 수열을 만들 수 있게 도와줘라.
'''

# 접근법
# 1. 맨앞의 수를 저장
# 2. 증가(1) 혹은 감소(-1) 여부 판별
# 3. 값을 하나씩 읽으면 부호가 바뀌는 순간 저장되어 있는 값과 비교
# 4. 부호에 따라 크기를 비교한다.
# 5. 같거나 부호가 유지된다면 index를 저장
# 6. 해당 인덱스까지 잘라서 뒤에 붙인다.
# 7. 부호가 바뀐다면 break
# 8. 인덱스 끝까지 읽었다면 탈출

# 예외처리 중요!!
'''
case 1.
10
3 3 3 3 4 3 3 3 3 3
=> 4가 정답 (5로 출력하지 않도록 주의)

case 2.
10
1 4 3 3 3 2 2 2 1 1
=> 1이 정답 (-1로 출력하지 않도록 주의)
'''

# 입력
N = int(input())
arr = list(map(int, input().split()))

# 읽기
K = 0
flow = 0
num = 0
pre = arr[0]
first = arr[0]
for i in range(len(arr)):
    # 증가, 감소 여부 정해졌는지 확인
    if flow:
        # 증가일 때
        if flow==1:
            # 감소를 만나면
            if arr[i] < pre:
                # 앞뒤값을 비교해서 조건만족
                if arr[i] <= first and arr[N-1] <= first and num==0:
                    num = 1
                    if arr[i]==first and arr[i]==arr[i-2] and arr[i]==arr[N-1]:
                      K = i-1
                    else:
                      K = i
                else:
                    K = -1
                    break
        # 감소일 때
        else:
            # 증가를 만나면
            if arr[i] > pre:
                # 앞뒤값을 비교해서 조건만족
                if arr[i] >= first and arr[N-1] >= first and num==0:
                    num = 1
                    if arr[i]==first and arr[i]==arr[i-2] and arr[i]==arr[N-1]:
                      K = i-1
                    else:
                      K = i
                else :
                    K = -1
                    break
    # 정해지지 않은 경우
    else:
        # 비교(값이 같은경우 걸러내기)
        if arr[i] > pre:
            flow = 1
        elif arr[i] < pre:
            flow = -1
    # 현재값을 이전값에 저장
    pre = arr[i]
print(K)