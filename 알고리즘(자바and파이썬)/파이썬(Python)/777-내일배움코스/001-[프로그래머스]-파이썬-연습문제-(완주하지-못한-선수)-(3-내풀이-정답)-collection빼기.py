# [프로그래머스]-파이썬-연습문제-(완주하지-못한-선수)-(3-내풀이-정답)-collection빼기.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 분 소요] / 총 풀이 시간[총 분 소요]


*** 참고


'''
#===================================================================================

import collections

def solution(participant, completion):

    answer = dict(collections.Counter(participant) - collections.Counter(completion))
    return list(answer.keys())[0]


#===================================================================================

# 예제 1
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion)) # "leo"

# 예제 2
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion)) # "vinko"

# 예제 3
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion)) # "mislav"

# def solution(participant, completion):
#     answer = ''
#     return answer