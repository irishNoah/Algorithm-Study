# 18258 / 큐 2 / S4
# https://www.acmicpc.net/problem/18258

# 시간 초과 판정이 나지 않게 하기 위해 input()으로 입력받는 것이 아닌
# sys.stdin.readline()을 통해 입력을 받고자 sys를 import한다.
import sys
# 파이썬으로 큐를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조를 활용하면 된다.
# duque는 스택과 큐의 장점을 모두 채택한 것인데, 데이터를 넣고 빼는 속도가 리스트 자료형에 비해
# 효율적이며 queue 라이브러리를 이용하는 것보다 더 간단하다.
from collections import deque

N = int(sys.stdin.readline())

# 큐 구현을 위해 deque 라이브러리를 사용함.
queue = deque()

for i in range(N) :
    command = sys.stdin.readline().split()

    if command[0] == "push" :
        queue.append(command[1])

    elif command[0] == "pop" :
        if len(queue) == 0 :
            print(-1)
        else :
            # 큐는 스택과 달리 맨 처음에 추가한 것이 가장 일찍 나오기 때문에
            # pop을 하려고 하면 pop() 함수가 아닌, popleft() 함수를 사용해야 한다.
            print(queue.popleft())
    
    elif command[0] == "size" :
        print(len(queue))

    elif command[0] == "empty" :
        if len(queue) == 0 :
            print(1)
        else :
            print(0)

    elif command[0] == "front" :
        if len(queue) == 0 :
            print(-1)
        else :
            print(queue[0])

    elif command[0] == "back" :
        if len(queue) == 0 :
            print(-1)
        else :
            print(queue[-1])