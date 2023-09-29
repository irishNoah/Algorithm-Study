# [프로그래머스]-파이썬-해시-(중복된-문자-제거)-LV1-(1-내풀이-정답)-collection활용.py
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/86051

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건(제한사항)
>>> 1 ≤ numbers의 길이 ≤ 9
>>> 0 ≤ numbers의 모든 원소 ≤ 9
>>> numbers의 모든 원소는 서로 다릅니다.

*** 설계 [총 2분 소요] / 총 풀이 시간[총 6분 소요]
- collection을 활용한다.

*** 정확성 테스트
- 100점
'''
# #############################################################
import collections

def solution(numbers):

    cnt_arr = collections.Counter([1,2,3,4,5,6,7,8,9,0])
    cnt_answer = collections.Counter(numbers)

    # 두 콜렉션을 뺄셈 연산한 이후, 키들의 합 구하기
    return sum(cnt_arr-cnt_answer)

# =========================================================

numbers = [1,2,3,4,6,7,8,0]
print(solution(numbers))
