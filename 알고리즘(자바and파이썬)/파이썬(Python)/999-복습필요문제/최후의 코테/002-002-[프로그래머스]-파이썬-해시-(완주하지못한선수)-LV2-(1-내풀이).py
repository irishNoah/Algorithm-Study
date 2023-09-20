'''
001-002-[프로그래머스]-파이썬-해시-(완주하지못한선수)-LV2-(1-내풀이)
- https://school.programmers.co.kr/learn/courses/30/lessons/42576
'''

import collections

def solution(participant, completion):
    answer = list(dict(collections.Counter(participant) - collections.Counter(completion)))

    return answer[0]