# [프로그래머스]-파이썬-문자열-(문자열-다루기-기본)-LV1-(2-내풀이-정답)-isdigit활용.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/12918?language=python3

'''
*** 참고 URL
https://appia.tistory.com/178

*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건(제한사항)
>>> 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인
>>> s는 길이 1 이상, 길이 8 이하인 문자열입니다.
>>> s는 영문 알파벳 대소문자 또는 0부터 9까지 숫자로 이루어져 있습니다.

*** 설계 [총 2분 소요] / 총 풀이 시간[총 8분 소요]
- isdigit()를 활용해 문자열이 숫자로만 구성되어 있는지 확인한다.
- len(s)가 4 또는 6인지 확인한다. 

*** 정확성 테스트
- 100점
'''
# #############################################################

def solution(s):
    return s.isdigit() and len(s) in [4, 6]

# =========================================================


s = "12345"

print(solution(s))