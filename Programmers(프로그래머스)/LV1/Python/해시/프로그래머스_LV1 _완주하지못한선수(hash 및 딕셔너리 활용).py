# 프로그래머스 LV1 - 완주하지 못한 선수(hash 및 딕셔너리 활용)
# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

def solution(participant, completion):
    answer = '' # 리턴할 값 answer

    hashDict = {}
    sumHash = 0

    '''
    participant의 각 리스트 값의 hash() 값을 hashDict 딕셔너리의 key에,
    participant의 각 리스트 값을 hashDict 딕셔너리의 value에 넣어준다.
    또한 hash() 함수를 통해 얻은 값을 sumHash에 더해준다.
    '''
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)

    '''
    completion 각 리스트 값의 hash() 값을
    sumHash의 값에서 차례대로 빼준다.
    이를 통해 누가 완주를 못했는지 알 수 있다.
    '''
    for comp in completion:
        sumHash -= hash(comp)

    # answer에 hashDict[sumHash], 즉 선수 이름을 대입한다.
    answer = hashDict[sumHash]

    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = 	["stanko", "ana", "mislav"]
print(solution(participant, completion))