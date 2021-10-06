# Programmers 입실 퇴실

from collections import deque

def solution(enter, leave):
    L = len(enter)
    enter = deque(enter)
    leave = deque(leave)
    meet = {i: set() for i in range(1, L+1)}
    answer = [0] * L
    students = set()
    # 퇴실 1번 확인
    while enter:
        a = leave.popleft()
        while a not in students:
            b = enter.popleft()
            # 만남 목록에 추가
            for s in students:
                meet[s].add(b)
                meet[b].add(s)
            students.add(b)
        students.remove(a)
    for key, value in meet.items():
        answer[key-1] = len(value)
    return answer