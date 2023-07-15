# [프로그래머스]-파이썬-연습-(평행)-LV0-(1-내풀이-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/120814

'''
*** 제한 > 시간 : 2초 (기본 1초) / 메모리 : 192MB (기본 128MB)

*** 조건
>>> dots의 길이 = 4
>>> dots의 원소는 [x, y] 형태이며 x, y는 정수입니다.
>>> 0 ≤ x, y ≤ 100
>>> 서로 다른 두개 이상의 점이 겹치는 경우는 없습니다.
>>> 두 직선이 겹치는 경우(일치하는 경우)에도 1을 return 해주세요.
>>> 임의의 두 점을 이은 직선이 x축 또는 y축과 평행한 경우는 주어지지 않습니다.

* 설계 [총 6분 소요] / 총 풀이 시간[총 13분 소요]
> 기울기 공식 = (y2-y1) / (x2-x1)
> 두 선 간 평행 공식 > 선A의 기울기 == 선B의 기술기

* 참고


'''
#===================================================================================

import sys

def solution(dots):

    if seek(dots[0], dots[1]) == seek(dots[2], dots[3]):
        return 1
    if seek(dots[0], dots[2]) == seek(dots[1], dots[3]):
        return 1
    if seek(dots[0], dots[3]) == seek(dots[1], dots[2]):
        return 1

    return 0

def seek(dotA, dotB): # 기울기 구하는 함수
    return (dotA[1]-dotB[1]) / (dotA[0]-dotB[0])



#===================================================================================
dots = [[1, 4], [9, 2], [3, 8], [11, 6]]
print(solution(dots)) # 1


# def solution(dots):
#     answer = 0
#     return answer