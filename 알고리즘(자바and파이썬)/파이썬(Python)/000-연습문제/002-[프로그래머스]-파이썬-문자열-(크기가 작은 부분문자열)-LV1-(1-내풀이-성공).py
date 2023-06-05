# [프로그래머스]-파이썬-문자열-(크기가 작은 부분문자열)-LV1-(1-내풀이-성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/147355

'''
# 문제 풀이
- 문자열 슬라이싱을 적절히 활용하면 good

'''

import sys

def solution(t, p):
    size = len(p)
    p = int(p)

    answer = 0
    for i in range(len(t)-size+1):
        part = t[i:i+size]

        if int(part) <= p:
           answer += 1

    return answer

t, p = map(str, sys.stdin.readline().split())
print(solution(t, p))