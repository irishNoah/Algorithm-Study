# [프로그래머스]-파이썬-연습문제-(삼총사)-LV1-(1-내풀이-성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/131705

'''
# 문제 풀이
1. 주어진 arr의 길이가 최대 13이니까 시간복잡도는 높아도 상관 x
2. 주어진 리스트에서 3개를 합쳐서 0이 나오도록 해야 한다? ---> 조합 사용하면 됨
3. 심지어, 서로 다른 학생의 정수 번호가 같을 수 있다.(= 중복 가능?) ---> 더더욱 조합
3. 참고로, 정수로 이루어진 조합은 sum() 활용 가능

'''

import sys
from itertools import combinations, permutations

def solution(arr):
    combi = list(combinations(arr, 3))

    # print(combi)

    cnt = 0

    for i in range(len(combi)):
        combi[i] = sum(combi[i])

        if combi[i] == 0:
            cnt += 1

    return cnt


arr = list(map(int, sys.stdin.readline().split()))
print(solution(arr))