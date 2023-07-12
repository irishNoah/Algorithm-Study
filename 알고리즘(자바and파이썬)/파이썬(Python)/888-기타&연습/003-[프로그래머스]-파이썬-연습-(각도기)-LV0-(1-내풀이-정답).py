# [프로그래머스]-파이썬-연습-(각도기)-LV0-(1-내풀이-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/120829

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)


*** 조건


* 설계 [총 2분 소요] / 총 풀이 시간[총 4분 소요]
-

'''
#===================================================================================

def solution(angle):
    answer = 0

    if 0 < angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif 90 < angle < 180:
        answer = 3
    elif angle == 180:
        answer = 4

    return answer


# #############################################################

angle = 91
print(solution(angle)) # 1