# BOJ 20207 달력

# 연속된 일정에 맞게 코팅지를 자르고 
# 1. 입력값을 리스트에 넣고 소팅 (2차원배열)
# 2. 빈리스트에 값을 하나씩 넣는다.
#  - 리스트 인덱스가 시작값, 숫자가 길이
# 3. for 반복문을 통해 숫자를 하나씩 꺼내서 리스트를 채운다.
# 4. 이 때, 열의 정보가 날짜, 행: 중복일정  => 채워진 리스트의 최대길이에 맞게 리스트를 구성한다. 
# 5. 이중 for문을 통해 한개열을 탐색하며 1을 만나면 1을 기록하고 다음열로
# 6. 숫자를 넣음으로써 마지막일정까지 체크했을 때, for문을 종료한다.(시간 감소)

cal = [0] * 365
for i in range(int(input())):
	a, b = map(int, input().split())
	for i in range(a, b+1):
		cal[i-1] += 1
total = 0
hgt = 0
wth = 0
for i in range(365):
	if cal[i] >= 1:
		wth += 1
		if cal[i] > hgt:
			hgt = cal[i]
	else:
		total += wth * hgt
		hgt = 0
		wth = 0
total += wth * hgt
print(total)