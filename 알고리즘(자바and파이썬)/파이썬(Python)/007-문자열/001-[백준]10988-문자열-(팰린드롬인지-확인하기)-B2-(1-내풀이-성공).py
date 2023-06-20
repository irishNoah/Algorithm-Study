# [백준]10988-문자열-(팰린드롬인지-확인하기)-B2-(1-내풀이-성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/10988

'''
# 문제 풀이

1. 입력된 문자열 길이를 확인한다.

* 문자열 길이가 홀수라면
> 가운데 글자의 인덱스를 확인 -> 가운데 글자 삭제 -> 문자열을 짝수로 맞추어준다.

* 문자열 길이가 짝수라면
> 그냥 그대로 진행

* for문 활용 > 범위 : 배열의 첫 번째부터 절반 요소까지
> arr[i] == arr[배열 길이-i]인지 확인
- 하나라도 틀린 게 있다면 : 0 출력
- for문 다 돌아도 틀린 게 없다면 : 1출력

'''
#============================================================

import sys

value = input() # level

if len(value) % 2 == 1:
    leng = len(value)//2

    value = value[:leng] + value[leng+1:]

flag = True
for i in range(len(value)//2):
    if value[i] != value[(len(value)-1)-i]:
        flag = False
        break

if flag == True:
    print(1)
else:
    print(0)
