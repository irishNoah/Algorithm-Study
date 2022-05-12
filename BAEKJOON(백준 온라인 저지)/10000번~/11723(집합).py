# https://github.com/irishNoah/Algorithm-Study
# 11723번 / 집합 / S5
# https://www.acmicpc.net/problem/11723

'''
해당 문제는 백준에서 6번 정도나 제출했다.
그 이유는 계속 런타임 에러가 발생했기 때문이다.
visual studio 상에서는 실행이 잘 됐는데
문제에서는 시간 제한을 1.5초로 설정했기 때문에 계속 런타임 에러가 뜬 것이다.

런타임 에러를 해결하기 위한 방안으로는 두 가지가 있었는데
첫 째는 sys 라이브러리의 스택을 사용하는 것이고
둘 째는 입력받은 tmp의 길이가 1이냐, 이것보다 큰 수냐에 따라 구분을 해 준 것이다.

만약 첫 째 방안만 하고 실행해도 런타임 에러가 발생하니
반드시 둘 째 방안까지 감안해야 런타임 에러가 발생하지 않는다.
'''

import sys

# 연산의 횟수 n 입력
n = int(sys.stdin.readline())

# 집합 자료형 변수 s 선언, s는 set()으로 초기화
s = set()

while 1:
    # 명령줄 입력
    tmp = sys.stdin.readline().strip().split() 

    # tmp의 길이가 1이면 command만 생성
    if len(tmp) == 1:
        command = tmp[0]
    # tmp의 길이가 1보다 크면 command, target 생성
    else:
        command, target = tmp[0], tmp[1]
        target = int(target)
    
    # 이하 명령어에 해당하는 과정은 기초 단계이므로 설명 생략
    if command == "add":
        s.add(target)
    
    elif command == "remove":
        s.discard(target)
    
    elif command == "check":
        print(1 if target in s else 0)

    elif command == "toggle":
        if target in s:
            s.discard(target)
        else:
            s.add(target)

    elif command == "all":
        s = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}

    elif command == "empty":
        s.clear()
    
    # 한 횟수를 실행할 때마다 n은 1 감소
    n = n-1

    # while문 탈출 조건
    if n == 0:
        break