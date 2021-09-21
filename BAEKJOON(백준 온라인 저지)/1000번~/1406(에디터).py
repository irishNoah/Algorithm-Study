# 1406 / 에디터 / S3
# https://www.acmicpc.net/problem/1406
# 참고 > https://kbwplace.tistory.com/87

# 기본적으로 스택(백준 10828) 문제 풀 듯이 풀었다.
# 이 문제를 코딩해서 VS CODE 상에서 실행했을 때는 문제 없이 출력이 잘 됐다.
# 하지만 백준에 문제 제출만 하면 시간 초과 판정이 났다. 즉, 문제 자체의 정답은
# 맞더라도, 시간 초과가 난 셈이었다.
# 아무리 sys를 활용해도 시간 초과가 해결되지 않았다.
# pop()과 append()도 잘 활용했다. 그럼에도 시간 초과가 해결되지 않았다.

# 자세히 보니 스택(백준 10828) 문제 풀 듯이 풀면 sys를 통해 시간 절약은 할 수 있지만
# 이 문제의 시간 제한은 0.3초이다. 그 이유는 내가 푼 방식의 알고리즘의 시간 복잡도는 O(N)이기 때문이다.
# 이 문제를 해결하기 위해서는 O(1)의 시간 복잡도를 구해야 한다.
# 이렇게 하기 위해서는 stack 구조를 한 개만 활용하면 안되고, 두 개를 활용해야 한다.
# 자세한 방식은 참고 사이트를 보면된다.

import sys

# 문자열 입력, readline() 자체는 enter{"\n"}도 입력으로 간주하기 때문에
# rstrip() 메소드를 활용하여 맨 오른쪽 문자를 제거해주기 때문에
# 이를 통해 enter를 제거한 채로 입력받을 수 있다.
stack_one = sys.stdin.readline().rstrip()

# 입력 받은 문자열을 리스트화
stack_one = list(stack_one)

# 두 개의 스택을 운영하여 문제를 풀어주기 위함
stack_two = [] 

# 명령어 개수 입력
commandValue = int(sys.stdin.readline())

# 입력받은 명령어의 개수 만큼 명령 실행
for i in range(commandValue) :
    # 명령에 대한 변수 command 선언 및 입력 받기
    command = sys.stdin.readline().split() # 한 줄 입력

    # L : 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
    if command[0] == "L" and stack_one :
       stack_two.append(stack_one.pop())

    # D : 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
    elif command[0] == "D" and stack_two:
        stack_one.append(stack_two.pop())

    # B : 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
    # 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 
    # 실제로 커서의 오른쪽에 있던 문자는 그대로임
    elif command[0] == "B" and stack_one :
        stack_one.pop()

    # P $ : $라는 문자를 커서 왼쪽에 추가함
    elif command[0] == "P" :
        stack_one.append(command[1])

print("".join(stack_one + list(reversed(stack_two))))