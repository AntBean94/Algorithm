# Programmers 스택/큐 기능개발

from collections import deque

def solution(progresses, speeds):
    answer = []
    task = deque(progresses)
    speeds = deque(speeds)
    while task:
        check = True
        today = 0
        for i in range(len(task)):
            task[i] += speeds[i]
            if task[i] >= 100 and check:
                today += 1
            else:
                check = False
        if today:
            answer.append(today)
            for i in range(today):
                task.popleft()
                speeds.popleft()
    return answer






test_case = [
    [[93, 30, 55], [1, 30, 5]],
    [[95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]]
]
for tc in test_case:
    print(solution(tc[0], tc[1]))