# [프로그래머스]-파이썬-문자열-(문자열-다루기-기본)-LV1-(1-내풀이-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/12918?language=python3

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건(제한사항)
>>> 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인
>>> s는 길이 1 이상, 길이 8 이하인 문자열입니다.
>>> s는 영문 알파벳 대소문자 또는 0부터 9까지 숫자로 이루어져 있습니다.

*** 설계 [총 2분 소요] / 총 풀이 시간[총 8분 소요]
-

*** 정확성 테스트
- 100점
'''
# #############################################################

def solution(s):
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    flag = True

    leng = len(s)

    if leng == 4 or leng == 6:

        for i in range(len(s)):
            if s[i] not in num:
                flag = False
                break

    else:
        flag = False

    return flag

# =========================================================


s = "1234"

print(solution(s))