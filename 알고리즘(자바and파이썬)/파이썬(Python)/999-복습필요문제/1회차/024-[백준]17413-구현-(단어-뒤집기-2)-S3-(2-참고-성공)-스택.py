# [백준]17413-구현-(단어-뒤집기-2)-S3-(2-참고-성공)-스택.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/17413

'''
*** 참고 URL
https://star7sss.tistory.com/391

*** 시간 : 1초 (기본 1초) / 메모리 : 512MB (기본 128MB)

*** 조건
>>> S의 길이는 100,000 이하
>>> 알파벳 소문자('a'-'z'), 숫자('0'-'9'), 공백(' '), 특수 문자('<', '>')로만 이루어져 있다.
>>> 문자열의 시작과 끝은 공백이 아니다.
>>> '<'와 '>'가 문자열에 있는 경우 번갈아가면서 등장하며, '<'이 먼저 등장한다. 또, 두 문자의 개수는 같다.

*** 설계 [총 9분 소요] / 총 풀이 시간[총 40분 소요]
>>>>> 메모리가 512MB이므로 for같은 거 많이 써도 된다는 뜻!

- 스택을 활용해서 풀었다.


'''
#============================================================

import sys
input = sys.stdin.readline

string = input().rstrip()
word_stack = []
tag = False
res = ''

for s in string:
    # 공백이면 word_stack 비움
    if s == " ":
        while word_stack:
            res += word_stack.pop()
        res += s

    # 태그 안 단어는 뒤집지 않음
    elif s == "<":
        while word_stack:
            res += word_stack.pop()
        tag = True
        res += s

    elif s == ">":
        tag = False
        res += s

    elif tag:
        res += s

    # 태그 밖 단어는 뒤집음
    else:
        word_stack.append(s)

    # print(res, tag)

# 출력
while word_stack:
    res += word_stack.pop()
print(res)