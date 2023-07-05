# [프로그래머스]-파이썬-해시-(중복된-문자-제거)-입문-(1-내풀이-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/120888

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건(제한사항)
>>> 1 ≤ my_string ≤ 110
>>> my_string은 대문자, 소문자, 공백으로 구성되어 있습니다.
>>> 대문자와 소문자를 구분합니다.
>>> 공백(" ")도 하나의 문자로 구분합니다.
>>> 중복된 문자 중 가장 앞에 있는 문자를 남깁니다.

*** 설계 [총 4분 소요] / 총 풀이 시간[총 7분 소요]
- 딕셔너리를 활용한다.

*** 정확성 테스트
- 100점

'''
# #############################################################

def solution(my_string):
    # answer = list(dict.fromkeys(my_string)) # 이것은 스트링 리스트 그 자체
    answer = "".join(list(dict.fromkeys(my_string)))  # 이거는 합친 거

    return answer

# =========================================================

my_string = "people"
print(solution(my_string))
