# [프로그래머스]-파이썬-정렬-(문자열-내-마음대로-정렬하기)-LV1-(1-내풀이-정답)-다중정렬.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/12915

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건
# 문제에서 중요한 조건만 따진다.

>>> 1<= strings <= 50
- 문자열로 구성된 리스트 strings의 길이가 최대 50이므로 O(N^3)의 시간복잡도를 구성할 수 있다.
>>> 모든 strings의 원소의 길이는 정수 n보다 크다.
- 즉, 문제될 사항이 없다.
>>> 인덱스 N의 문자가 같은 문자열이 여럿일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치한다.
- 즉, 다중 정렬을 사용하여라
    - 다중 정렬 시간 복잡도는 O(N*logN)  

*** 설계 [총 10분 소요] / 총 풀이 시간[총 13분 소요]


'''
#===================================================================================

def solution(strings, n):
    # 우선 strings의 각 문자열에서 인덱스 n의 사전순대로 먼저 정렬하되
    # 인덱스 n의 알파벳이 동일할 경우, 문자열 자체 사전순으로 다중 정렬화 해주었다.
    answer = sorted(strings, key=lambda x:(x[n], x))
    return answer


#===================================================================================

# 예제 1
strings = ["sun", "bed", "car"]
n = 1
print(solution(strings, n)) # ["car", "bed", "sun"]

# 예제 2
strings = ["abce", "abcd", "cdx"]
n = 2
print(solution(strings, n)) # ["abcd", "abce", "cdx"]

# def solution(strings, n):
#     answer = []
#     return answer