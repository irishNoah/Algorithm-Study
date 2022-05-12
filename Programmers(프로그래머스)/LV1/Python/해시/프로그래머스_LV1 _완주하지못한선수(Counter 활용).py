# 프로그래머스 LV1 - 완주하지 못한 선수(Counter 활용)
# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
import collections

def solution(participant, completion):
    answer = '' # 리턴할 값 answer

    '''
    participant와 completion 길이의 차는 1이다.
    이를 활용하기 위해 Counter 클래스를 활용하면 된다.
    participant와 completion 배열 간의 차를 구하고
    마지막 Counter에서 Key 값을 읽어오기 위해 list(value.keys())[0]를 answer에 대입한다.
    '''
    value = collections.Counter(participant) - collections.Counter(completion)

    answer = list(value.keys())[0]


    return answer

participant = ["mislav", "stanko", "mislav", "ana"]
completion = 	["stanko", "ana", "mislav"]
print(solution(participant, completion))