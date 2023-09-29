# [프로그래머스]-파이썬-연습문제-(완주하지-못한-선수)-(1-내풀이-정답)-Counter활용.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/134240

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건


*** 설계 [총 15분 소요] / 총 풀이 시간[총 35분 소요]
- 처음에는, 동명이인이 있을 경우, 동명이인 중 한 명이 완주를 하지 못했다고 가정하고 풀었다.
- 하지만, 동명이인이 모두 완주할 수도 있기 때문에 몇 가지의 테스트에서 틀린 것이었다.
- 따라서, collection을 구해서 차집합으로 푸는 게 정답이다.

*** 참고
https://pydole.tistory.com/entry/Python-collections-Counter%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%95%A9%EC%A7%91%ED%95%A9-%EA%B5%90%EC%A7%91%ED%95%A9-%EC%B0%A8%EC%A7%91%ED%95%A9-%EA%B5%AC%ED%95%98%EA%B8%B0
'''
#===================================================================================
import collections

def solution(participant, completion):
    ctParti = collections.Counter(participant)
    ctComp = collections.Counter(completion)

    # print(ctParti-ctComp) >>> Counter({'mislav': 1}) 형식으로 출력됨
    answer = list((ctParti-ctComp).elements())
    return answer[0]


#===================================================================================

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["mislav", "stanko", "ana"]

print(solution(participant, completion)) # "mislav"

# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]

# print(solution(participant, completion)) # "leo"

# def solution(participant, completion):
#     answer = ''
#     return answer