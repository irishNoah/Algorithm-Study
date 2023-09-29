# [프로그래머스]-파이썬-탐욕법-(체육복)-(2-강사풀이(2))-set활용.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 분 소요] / 총 풀이 시간[총 분 소요]

*** 참고

'''
#===================================================================================

def solution(n, lost, reserve):
    # set > O(N)
    s = set(lost) & set(reserve) # lost와 reserve의 교집합을 찾는다.
    l = set(lost) - s # lost와 s의 차집합을 구한다. >>> 확실히 빌려야 하는 명단
    r = set(reserve) - s # reserve와 s의 차집합을 구한다. >>> 확실히 빌려줄 수 있는 명단

    # sorted() > O(N * logN)
    for x in sorted(r): # 먼저 정렬해주기!
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remove(x+1)

    return n - len(l)


#===================================================================================

# 예제 1
n = 5
lost = [2, 4]
reserve = [1, 3, 5]
print(solution(n, lost, reserve)) # 5

# 예제 2
n = 5
lost = [2, 4]
reserve = [3]
print(solution(n, lost, reserve)) # 4

# 예제 3
n = 3
lost = [3]
reserve = [1]
print(solution(n, lost, reserve)) # 2

# def solution(n, lost, reserve):
#     answer = 0
#
#     return answer