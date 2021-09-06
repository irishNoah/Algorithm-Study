# 10845 / 큐 / S4
# https://www.acmicpc.net/problem/10845

import sys # 메모리 초과 판정을 받지 않기 하게 위하여 sys를 import
# queue를 구현하기 위해 deque 라이브러리를 할당
from collections import deque

# 명령의 개수 n 입력
n = int(input())

# 큐를 구현하기 위해 deque() 할당
queue = deque()

for i in range(n):
    # 명령 입력
    command = sys.stdin.readline().split()

    if command[0] == "push" : # push일 경우
        queue.append(command[1]) # 입력받은 수를 queue에 할당

    elif command[0] == "pop" : # pop일 경우
        if len(queue) == 0 : # queue의 길이가 0이면 -1 출력
            print(-1)
        
        else : # 길이가 0이 아니면 가장 앞에 있는 숫자를 출력후 그 수를 queue에서 뺀다.
            print(queue.popleft())

    elif command[0] == "size" : # size일 경우
        print(len(queue)) # queue의 길이를 출력

    elif command[0] == "empty" : # empty일 경우
        if len(queue) == 0 : # 길이가 0이면 1을 출력
            print(1)
        
        else : # 길이가 0이 아니면 0을 출력
            print(0)

    elif command[0] == "front" : # front일 경우
        if len(queue) == 0 : # 길이가 0이면 -1 출력
            print(-1)
        
        else : # 길이가 0이 아니면 queue의 가장 앞에 있는 수를 출력
            print(queue[0])

    elif command[0] == "back" : # back 경우
        if len(queue) == 0 : # 길이가 0이면 -1 출력
            print(-1)
        
        else : # 길이가 0이 아니면 queue의 가장 뒤에 있는 수를 출력
            print(queue[-1])