# [프로그래머스]-파이썬-탐욕법-(체육복)-(2-강사풀이(1))-리스트.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 분 소요] / 총 풀이 시간[총 분 소요]

*** 참고
- 해당 문제풀이는 for x in range(1, n+1) 로 인해 O(N)의 시간 복잡도를 가짐


'''
#===================================================================================

def solution(n, lost, reserve):
    cloth = [1]*(n+2) # 인덱스 에러 방지하기 위해 n보다 2만큼 더 크게 생성

    for x in lost:
        cloth[x] -= 1
    for x in reserve:
        cloth[x] += 1

    answer = 0
    # 체육복 빌림 구하기
    for x in range(1, n+1):
        # 인덱스가 1~(마지막-1) 에 해당
        if cloth[x-1] == 0 and cloth[x] ==2:
            cloth[x-1] = 1; cloth[x] = 1

        if cloth[x] == 2 and cloth[x+1] == 0:
            cloth[x] = 1; cloth[x+1] = 1


    answer = len([x for x in cloth[1:-1] if x > 0])
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

# def solution(n, lost, reserve):
#     answer = 0
#
#     return answer