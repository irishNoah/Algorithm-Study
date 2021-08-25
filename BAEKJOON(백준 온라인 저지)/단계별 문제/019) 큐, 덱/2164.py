# 2164 / 카드2 / S4
# https://www.acmicpc.net/problem/2164

import sys
# 파이썬으로 queue를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조를 활용하면 된다.
from collections import deque

N = int(sys.stdin.readline())

# 큐를 구현하기 위해 데크 라이브러리 사용
queue = deque()

# 입력받은 N만큼 1부터 N까지 1의 등차만큼 차례대로 queue에 append 해줌 
for i in range(1, N+1) :
    queue.append(i)

while True :
    # queu의 길이가 1 이하면 while문 탈출
    if len(queue) <= 1 :
        break

    # 제일 위에 있는 숫자를 버리기 위해 popleft() 실행
    queue.popleft()

    # 이후에 제일 위해 있는 숫자를 맨 뒤로 옯기기 위해 
    # 변수 x에 queue[0]을 할당
    x = queue[0]
    # 그 x를 queue에 append() 실행
    queue.append(x)
    # 그리고 기존 queue[0]을 popleft()를 통해 제거
    queue.popleft()

# 마지막으로 남은 한 카드를 출력
print(queue[0])