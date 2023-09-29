# [백준]10448-완전탐색-(유레카-이론)-B1-(1-내풀이-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/10448

'''
* 제한 > 시간 : 1초 / 메모리 : 256MB
- 시간 제한이 1초
- 하지만, 메모리가 128MB에서 256으로 증가
- 자연수 K의 범위(3 <= K <= 1000)
- 자연수의 범위가 적은 것을 보아 탐색...?

* 설계
> 삼각수의 값이 1000 직전인데까지 삼각수 함수에 대입
> 조합으로 3개 해서 합이 입력된 수와 동일한게 하나라도 있다면 1 출력
- 문제에서 "3개의 삼각수가 모두 달라야 할 필요는 없다." 라고 언급
- 즉, 동일한 삼각수가 1번이든, 2번이든, 3번이든 쓰일 수 있다는 의미
- 이런 경우, itertools.combinations_with_replacement() 메소드 사용
> 없으면 0 출력

'''
#============================================================

import sys
import itertools

# 삼각수 리스트 생성
samgak = []; n = 1
while True:
    val = (n*(n+1)) / 2

    if val > 1000:
        break

    samgak.append(val)
    n = n+1

arr = list(itertools.combinations_with_replacement(samgak, 3))

case = int(sys.stdin.readline().rstrip())

for _ in range(case):
    case = case - 1

    num = int(sys.stdin.readline().rstrip())

    flag = False

    for i in range(len(arr)):
        if sum(arr[i]) == num:
            flag = True
            print(1)
            break

    if flag == False:
        print(0)

    if case == 0:
        break