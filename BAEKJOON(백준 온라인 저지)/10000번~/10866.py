# 10866 / 덱 / S4
# https://www.acmicpc.net/problem/10866

import sys
# 파이썬으로 deque를 구현할 때는 collections 모듈에서 제공하는 deque 자료구조를 활용하면 된다.
from collections import deque

N = int(sys.stdin.readline())

# 데크 구현을 위해 deque 라이브러리를 사용함.
deq = deque()

for i in range(N) :
    command = sys.stdin.readline().split()

    if command[0] == "push_front" :
        # 덱의 앞에 값을 넣기 위해서는 appendleft() 함수를 사용해야 함
        deq.appendleft(command[1])

    elif command[0] == "push_back" :
        # 덱의 뒤에 값을 넣기 위해서는 append() 함수를 사용해야 함
        deq.append(command[1])

    elif command[0] == "pop_front" :
        if len(deq) == 0 :
            print(-1)
        else :
            # 덱의 가장 앞에 있는 수를 빼기 위해서는 popleft() 함수를 사용해야 함
            print(deq.popleft())

    elif command[0] == "pop_back" :
        if len(deq) == 0 :
            print(-1)
        else :
            # 덱의 가장 뒤에 있는 수를 빼기 위해서는 pop() 함수를 사용해야 함
            print(deq.pop())
    
    elif command[0] == "size" :
        print(len(deq))

    elif command[0] == "empty" :
        if len(deq) == 0 :
            print(1)
        else :
            print(0)

    elif command[0] == "front" :
        if len(deq) == 0 :
            print(-1)
        else :
            print(deq[0])

    elif command[0] == "back" :
        if len(deq) == 0 :
            print(-1)
        else :
            print(deq[-1])