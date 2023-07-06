# [백준]17413-구현-(단어-뒤집기-2)-S3-(1-내풀이-실패).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/17413

'''
*** 참고 URL

*** 시간 : 1초 (기본 1초) / 메모리 : 512MB (기본 128MB)

*** 조건
>>> S의 길이는 100,000 이하
>>> 알파벳 소문자('a'-'z'), 숫자('0'-'9'), 공백(' '), 특수 문자('<', '>')로만 이루어져 있다.
>>> 문자열의 시작과 끝은 공백이 아니다.
>>> '<'와 '>'가 문자열에 있는 경우 번갈아가면서 등장하며, '<'이 먼저 등장한다. 또, 두 문자의 개수는 같다.

*** 설계 [총 9분 소요] / 총 풀이 시간[총 40분 소요]
>>>>> 메모리가 512MB이므로 for같은 거 많이 써도 된다는 뜻!
>>> 답 문자열 answer

1. 문자열에서 '<'를 만나면 '>'를 만날 때까지 계속 answer에 더한다.
2. 공백일 경우
3. '<', '>' 안에 없는 문자나 숫자는 공백 또는 '<'를 만나기 직전까지
word라는 문자열에 더해준다.
    > 그러다가 만나면 word를 reverse 해준 이후, 이를 answer에 더해준다.

*** 왜 틀렸을까?
- 예제 1~6에서 입력 5에 대한 결과만 틀린다.
- 실제 python의 태그와 겹처서 일까?

'''
#============================================================

import sys

# arr = "<problem>17413<is hardest>problem ever<end>"
arr = sys.stdin.readline().rstrip()

answer = ""
word = "" # # 태그(< > )안에 없는 문자열에 대해 역순을 구하기 위한 문자열

flag = False # 태그(< > )안에 있는지 확인하기 위한 변수 / False일 때에는 태그 안에 없는 것
for i in range(len(arr)):
    if arr[i] == "<":
        if word != "":
            answer += word[::-1]
            word = ""

        flag = True
        answer += arr[i]
        continue

    if flag == True:
        if arr[i] == ">":
            flag = False

        answer += arr[i]
        continue

    if flag == False:
        if arr[i] == " " or i == (len(arr)-1):
            # 공백 이전까지 저장됐던 문자열이 있다면 또는 인덱스가 마지막 이라면, 역순으로 해서 answer에 더하기
            if word != "":
                answer += word[::-1]
                word = ""

            answer += arr[i]

        else:
            word += arr[i]

print(answer)