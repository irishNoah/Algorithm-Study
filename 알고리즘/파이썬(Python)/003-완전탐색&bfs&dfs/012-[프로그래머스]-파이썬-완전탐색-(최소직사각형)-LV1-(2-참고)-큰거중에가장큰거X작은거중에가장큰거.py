# [프로그래머스]-파이썬-완전탐색-(최소직사각형)-LV1-(2-참고)-큰거중에가장큰거X작은거중에가장큰거.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/86491

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)


*** 조건
sizes의 길이는 1 이상 10,000 이하입니다.
sizes의 원소는 [w, h] 형식입니다.
w는 명함의 가로 길이를 나타냅니다.
h는 명함의 세로 길이를 나타냅니다.
w와 h는 1 이상 1,000 이하인 자연수입니다.

*** 설계 [총 분 소요] / 총 풀이 시간[총 분 소요]

*** 다른 풀이
반 나눠서 큰거중에 가장 큰거 * 작은거중에 가장 큰거

'''
#===================================================================================

def solution(sizes):
    # 반 나눠서 큰거중에 가장 큰거 * 작은거중에 가장 큰거
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)


# #############################################################

sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(sizes))