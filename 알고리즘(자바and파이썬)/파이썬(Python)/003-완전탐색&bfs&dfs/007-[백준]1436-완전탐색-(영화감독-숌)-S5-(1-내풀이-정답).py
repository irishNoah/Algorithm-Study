# [백준]1436-완전탐색-(영화감독-숌)-S5-(1-내풀이-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1436

'''
* 제한 > 시간 : 2초 / 메모리 : 128MB
- 제한시간 2초
- 입력값은 1개, 출력값은 1개
- 입력값 <= 10000
- 시간제한과 데이터의 개수 및 범위를 감안했을 때 탐색일 가능성 있음

* 설계 [총 15분 소요] / 총 풀이 시간[총 27분 소요]
> Python 3부터는 정수형 데이터의 크기에 제한이 없다
> 정수 N을 입력을 한다.
> while문을 활용한다.
1. num(정수)의 초기값 : 666
2. num to str
- str된 num에 666이 들어가 있으면 정수 N에서 -1 하기
3. N이 0이 되면
위 666들어가 있는 num을 결과 res에 할당 & 출력 & while문 종료


'''
#============================================================

import sys

n = int(sys.stdin.readline().rstrip())

if n == 1:
    print(666)
else:
    n = n-1
    num = 1665; res = 0

    while True:
        num = num+1

        if "666" in str(num):
            n = n-1

            if n == 0:
                res = num
                print(res)
                break