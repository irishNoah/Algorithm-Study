# [백준]20055-구현-(컨베이어-벨트-위의-로봇)-G5-(2-참고-).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/20055

'''
# 문제 풀이

> 참고 URL : https://ryu-e.tistory.com/116

> 회전을 쉽게 하기 위해 deque를 사용한다.
? n개의 벨트만 로봇이 존재할 수 있음 ⇒ n길이의 로봇 유무를 저장하는 배열을 만든다.
1. 벨트를 회전한다. ⇒ deque rotate사용
2. 로봇 이동하기
- 가장 먼저 올라간 로봇부터 앞으로 이동
- 다음칸이 내구도 존재하고, 로봇도 없고, 현재 로봇이 존재하는 경우 진행
3. 올리는 위치에 내구도 0이 아니고, 로봇이 처음에 존재하지 않으면 로봇 올리기
4. 내구도 0인 칸 수가 k이상이면 그만

'''

from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
a = deque(map(int, sys.stdin.readline().split()))  # 내구도. A1, A2, ..., A2N
robot = deque([0] * n)  # 벨트위에 있는 로봇
result = 0

#============================================================

while True:
    result += 1

    # 1. 벨트 회전한다.
    a.rotate(1)
    robot[-1] = 0
    robot.rotate(1)
    robot[-1] = 0    # 내리는 위치에 도달한 경우, 즉시 내림

    # 2. 로봇 이동하기. 이동하려는 칸에 로봇 x, 내구도 1이상 남아야함.
    for i in range(n - 2, -1, -1):  # 먼저 올라간 로봇부터 진행
        if a[i + 1] >= 1 and robot[i + 1] == 0 and robot[i] == 1:
            robot[i + 1] = 1
            robot[i] = 0
            a[i + 1] -= 1
    robot[-1] = 0  # 내리는 위치에 도달한 경우, 즉시 내림

    # 3. 올리는 위치에 내구도 0 아니면 로봇 올리기 & 내구도 감소
    if a[0] != 0 and robot[0] != 1:
        robot[0] = 1
        a[0] -= 1

    # 4. 내구도 0인 칸 수가 k이상이면 종료
    if a.count(0) >= k:
        break

print(result)