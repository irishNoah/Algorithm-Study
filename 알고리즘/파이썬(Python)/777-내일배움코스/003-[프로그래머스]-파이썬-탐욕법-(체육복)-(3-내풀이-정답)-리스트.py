# [프로그래머스]-파이썬-탐욕법-(체육복)-(3-내풀이-정답)-리스트.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 분 소요] / 총 풀이 시간[총 분 소요]

*** 참고
'''
#===================================================================================

def solution(n, lost, reserve):
    answer = 0

    check = [1] * (n+2)

    for val in lost:
        check[val] -= 1
    for val in reserve:
        check[val] += 1

    for i in range(1, n+1): # 방향성이 중요 >>> 왼쪽 먼저 확인한다.
        if check[i] == 0 and check[i+1] == 2:
            check[i] = 1; check[i+1] = 1
        if check[i] == 2 and check[i+1] == 0:
            check[i] = 1; check[i+1] = 1

        if check[i] > 0:
            answer += 1

    return answer

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

# 예제 4
n = 5
lost = [1,3]
reserve = [2,4]
print(solution(n, lost, reserve)) # 5

# def solution(n, lost, reserve):
#     answer = 0
#
#     return answer