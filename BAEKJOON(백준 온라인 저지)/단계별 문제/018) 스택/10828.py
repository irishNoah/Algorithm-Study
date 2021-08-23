# 10828 / 스택 / S4
# https://www.acmicpc.net/problem/10828

# 시간 초과 판정이 나지 않게 하기 위해 input()으로 입력받는 것이 아닌
# sys.stdin.readline()을 통해 입력을 받고자 sys를 import한다.
import sys

# 명령의 수 N
N = int(sys.stdin.readline())

# 스택 리스트 stack 선언
stack = []

# for문으로 입력을 받고, 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력
for i in range(N) :
    command = sys.stdin.readline().split() # 한 줄 입력

    if command[0] == "push" : # push를 입력받은 경우
        stack.append(command[1]) # 그 이후에 오는 숫자를 append 함

    elif command[0] == "pop" : # pop을 입력받은 경우
        # stack의 길이가 0이면 -1 출력
        if len(stack)==0:
            print(-1)

        # 길이가 0보다 크면 가장 마지막 추가 값 출력 후 pop()을 통해 제거
        else :
            print(stack.pop())

    # size를 입력 받은 경우 말 그대로 stack의 길이 출력
    elif command[0] == "size" :
        print(len(stack))

    elif command[0] == "empty" : # empty를 입력받은 경우 
        # 길이가 0이면 1 출력
        if len(stack) == 0 :
            print(1)
        # 길이가 0이 아니면 0출력
        else :
            print(0)

    elif command[0] == "top" : # top을 입력받은 경우 
        if len(stack)==0: # 길이가 0이면 -1 출력
            print(-1)
        else: # stack 리스트의 마지막 원소 출력
            print(stack[-1])