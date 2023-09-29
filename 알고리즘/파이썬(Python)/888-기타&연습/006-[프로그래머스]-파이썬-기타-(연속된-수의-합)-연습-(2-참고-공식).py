# [프로그래머스]-파이썬-기타-(연속된-수의-합)-연습-(2-참고-공식).py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/120923

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)


*** 조건


* 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
-

'''
#===================================================================================

def solution(num, total):
    answer = []
    var = sum(range(num+1))
    diff = total - var
    start_num = diff//num
    answer = [i+1+start_num for i in range(num)]
    return answer

# #############################################################

