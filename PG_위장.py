# Programmers 해시 위장

def solution(clothes):
    answer = 1
    closet = dict()
    for i in clothes:
        if i[1] in closet:
            closet[i[1]] += 1
        else:
            closet[i[1]] = 1
    for i in closet.values():
        answer *= (i + 1)
    answer -= 1
    return answer


test_case = [
    [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]],
    [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
]
for tc in test_case:
    print(solution(tc))