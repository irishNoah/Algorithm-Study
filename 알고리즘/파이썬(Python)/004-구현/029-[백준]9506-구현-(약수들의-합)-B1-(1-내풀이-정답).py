# [백준]9506-구현-(약수들의-합)-B1-(1-내풀이-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/9506

'''
*** 참고 URL

*** 시간 : 1초 (기본 2초) / 메모리 : 128MB (기본 128MB)

*** 조건

*** 설계 [6분 소요] / 총 풀이 시간[총 25분 소요]
- 수 num을 입력 받는다.
    - 단, num이 -1이면 시스템 종료
- result = str(num) + " = " 할당
- for
    - range(1, num)
        - val로 나눈 나머지가 0이면 약수
            - result += " " + str(val) + " " 할당
            - sumVal += val
- 만약 sumVal == num
    - 참이면 결과 출력
    - 거짓이면
        - 완전수 아닌 멘트 출력

### 후기
- 초기에는 각 num이나 for문의 i를 str 타입으로 해서 출력 형식이 잘못됐다고 했음
- 그래서, 숫자에 대해서는 int 타입으로 하였음
- but, 띄어쓰기 때문에 또 출력 형식이 잘못됐다고 했음

'''
#============================================================

import sys

while True:
    num = int(sys.stdin.readline().rstrip())
    if num == -1:
        break

    divVal = []
    for i in range(1, num):
        if num % i == 0:
            divVal.append(i)

    if sum(divVal) == num:
        print(num, "=", end=" ")

        for j in range(len(divVal)):
            if j == len(divVal)-1:
                print(divVal[j])
            else:
                print(divVal[j], end=" + ")

    else:
        print(num, "is NOT perfect.")