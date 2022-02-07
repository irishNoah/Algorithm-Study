# 프로그래머스 LV1 - 완주하지 못한 선수(초기 풀이)
# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

'''
처음 풀었을 때는 아래와 같이 풀었음
해당 문제는 정확성 테스트에서 80점, 효율성 테스트에서 80점을 맞았음
중복된 선수를 비교할 때 for문을 사용한 것이 테스트에서 100점을 맞지 못한 이유로 생각함
'''

from collections import Counter

def solution(participant, completion):
    answer = '' # 리턴할 값 answer

    '''
    participant와 completion를 딕셔너리로 비교하기 위해
    두 리스트를 딕셔너리 자료형으로 만들어준다.
    participant의 딕셔너리 자료형은 dic_participant이며
    completion를 딕셔너리 자료형은 dic_completion
    '''
    dic_participant = {string : 0 for string in participant}
    dic_completion = {string : 0 for string in completion}

    '''
    두 딕셔너리의 키값 비교를 통해 누가 완주를 못했는지 판별하고자
    각 딕셔너리 자료형의 키값만 가지고 있는 리스트를 선언
    dic_participant의 키값 리스트는 keys_participant
    dic_completion의 키값 리스트는 keys_completion
    '''
    keys_participant = set(list(dic_participant.keys()))
    keys_completion = set(list(dic_completion.keys()))

    # 키 값을 뺀 이후에 반환값은 문자열로 해주기 위해 join 메소드 사용
    answer = list(keys_participant - keys_completion)
    answer = ''.join(answer)

    # 만약 중복된 이름 중 완주하지 못할 경우 Counter 메소드를 활용하여 해결
    if len(answer) == 0:
        result_value = Counter(participant)

        for key, value in result_value.items():
            if value >= 2:
                answer = key

    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = 	["stanko", "ana", "mislav"]
print(solution(participant, completion))