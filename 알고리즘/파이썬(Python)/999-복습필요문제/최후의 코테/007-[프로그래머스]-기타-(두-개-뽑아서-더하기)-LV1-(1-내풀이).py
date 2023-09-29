'''
007-[프로그래머스]-기타-(두-개-뽑아서-더하기)-LV1-(1-내풀이).py

- https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3
'''

from itertools import permutations


def solution(numbers):
    
    # permutations든 combinations든 해당 문제에서는 상관 X
    num = list(permutations(numbers, 2))
    arr = []
    
    # 순열 또는 조합으로 구해진 각 2차원 배열에서 각 배열의 합을 구해 arr에 넣기
    for cnt in num:
        arr.append(cnt[0] + cnt[1])
    
    # 오름차순으로 정렬 / set 화
    return sorted(list(set(arr)))