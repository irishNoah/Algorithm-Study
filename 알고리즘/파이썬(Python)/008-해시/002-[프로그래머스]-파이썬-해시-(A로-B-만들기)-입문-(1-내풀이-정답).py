# [프로그래머스]-파이썬-해시-(A로-B-만들기)-입문-(1-내풀이-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/120886

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건(제한사항)
>>> 0 < before의 길이 == after의 길이 < 1,000
>>> before와 after는 모두 소문자로 이루어져 있습니다.

*** 설계 [총 2분 소요] / 총 풀이 시간[총 7분 소요]
- before와 after를 모두 리스트화
- 둘 다 정렬 >>> sorted() 활용
- 정렬한 게 같으면 1, 다르면 0

*** 정확성 테스트
- 100점

'''
# #############################################################

def solution(before, after):
    answer = -1

    list_bef = list(before)
    list_aft = list(after)

    if sorted(list_bef) == sorted(list_aft):
        answer = 1
    else:
        answer = 0

    return answer


# =========================================================

before = "olleh"; after = "hello"
print(solution(before, after))
