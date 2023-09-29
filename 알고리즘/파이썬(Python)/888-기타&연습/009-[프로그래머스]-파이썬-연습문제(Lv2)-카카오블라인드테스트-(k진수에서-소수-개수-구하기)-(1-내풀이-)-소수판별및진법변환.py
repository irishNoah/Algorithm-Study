# [프로그래머스]-파이썬-연습문제(Lv2)-카카오블라인드테스트-(k진수에서-소수-개수-구하기)-(1-내풀이-)-소수판별및진법변환
# https://github.com/irishNoah/Algorithm-Study
# https://school.programmers.co.kr/learn/courses/30/lessons/92335

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 5분 소요] / 총 풀이 시간[총 45분 소요]
- 우선, 정수 n에 대하 원하는 진수 k법으로 변환한다.
- 변환된 k법의 수 중간에 "0"이 있는 것을 제거하기 위해 split("0")으로
구분하여 문자열로 구성된 리스트에 할당한다.
    - 단, "0"으로 분할한 문자열 리스트의 구성 요소 중에서
    "1"이거나 None일 경우에는 할당하지 않는다.
- 최종적으로 구해진 리스트의 구성 요소 중에서 소수인지 아닌지 판별한다.
    - 판별해서 소수에 해당될 경우 answer을 1 증가한다. 

*** 참고
> 원하는 진수로 변환하기
- https://security-nanglam.tistory.com/508

> 소수의 판별(개선된 알고리즘)
- https://freedeveloper.tistory.com/391
'''
#===================================================================================

import string
import math

tmp = string.digits + string.ascii_lowercase
def convert(n, k): # 진법 변환 함수 / 시간복잡도 > O(N)
    q, r = divmod(n, k)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, k) + tmp[r]

def is_prime_number(x): # 개선된 소수 판별 알고리즘 / 시간복잡도 > O(N) 미만
    # 2부터 num의 제곱근까지 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x))+1):
        # x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

def solution(n, k):
    answer = 0

    ### 진법 변환
    base = convert(n, k) # base의 타입 > str

    ### "0"으로 슬라이싱하되, 슬라이싱한 것이 "1"또는 None이 아닌 경우
    ### 소수 판별 알고리즘 진행
    for x in base.split("0"):
        if x != "1" and x != '': # and와 or 사용 주의하기
            if is_prime_number(int(x)) == True:
                answer += 1

    return answer

#===================================================================================

# 예제 1
n = 437674
k = 3
print(solution(n, k)) # 3

# 예제 2
n = 110011
k = 10
print(solution(n, k)) # 2

# def solution(n, k):
#     answer = -1
#     return answer