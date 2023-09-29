# [백준]17413-구현-(단어-뒤집기-2)-S3-(3-내풀이-정답)-for문 활용.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/17413

'''
*** 참고 URL

*** 시간 : 1초 (기본 1초) / 메모리 : 512MB (기본 128MB)

*** 조건


*** 설계 [ 6분 소요] / 총 풀이 시간[총 19분 소요]
- flag를 활용한다.
    - 태그(<, >)안에 있는 상황이라면
        - '<'를 만났을 때 flag = True / '>'를 만났을 때 '>'까지 answer에 더해주고 flag = False ()
- flag
    - True라면 answer에 그대로 더해주기
    - False라면 word라는 문자열 변수에 더해주기
        - '<'를 만날 때 word가 비어 있지 않으면 word[::-1]를 통해 answer에 더해주고, word 초기화
    - 만약, False 상태에서 공백이 있다면?
        - 공백을 만날 때까지 word 더해주기
            - 단, 공백은 안만났는데, 마지막 인덱스를 만나게 된다면
                - word[::-1]를 통해 answer에 더해주기
        - 공백 만나게 되면
            - word[::-1]를 통해 answer에 더해주고, word 초기화
            - 공백은 그대로 더해주기

'''
#============================================================

import sys

val = sys.stdin.readline().rstrip()
flag = False

answer = ""; word = ""
for i in range(len(val)):
    if val[i] == "<":
        if word != "":
            answer += word[::-1]
            word = ""

        answer += val[i]
        flag = True

    elif val[i] == ">":
        answer += val[i]
        flag = False

    else:
        if flag == True:
            answer += val[i]

        else:
            if val[i] != " ":
                word += val[i]

                if i == len(val)-1:
                    answer += word[::-1]

            else:
                if word != "":
                    answer += word[::-1]
                    word = ""

                answer += val[i]

print(answer)