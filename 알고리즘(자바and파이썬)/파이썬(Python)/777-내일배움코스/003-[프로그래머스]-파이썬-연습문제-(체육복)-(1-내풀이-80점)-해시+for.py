# [프로그래머스]-파이썬-탐욕법-(체육복)-(1-내풀이-80점)-해시+for.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 분 소요] / 총 풀이 시간[총 분 소요]
- 해시로 학생 수만큼 생성, 생성 때부터 값을 1로 세팅
    - lost에 있으면 -1 / reserve에 있으면 +1

*** 참고
'''
#===================================================================================

def solution(n, lost, reserve):
    cloth = {}

    # 체육복 상황 구하기
    for x in range(0, n+2):
        cloth[x] = cloth.get(x, 0) + 1

        if x in lost:
            # print(x)
            cloth[x] -= 1
        if x in reserve:
            # print(x)
            cloth[x] += 1
    # print(cloth)
    # print(cloth[3])

    answer = 0
    # 체육복 빌림 구하기
    for x in range(1, n+1):
        # 인덱스가 1~(마지막-1) 에 해당
        if cloth[x] == 0:
            if cloth[x+1] == 2:
                cloth[x] += 1
                cloth[x+1] -= 1

        if cloth[x] == 0:
            if cloth[x - 1] == 2:
                cloth[x] += 1
                cloth[x - 1] -= 1

        if cloth[x] > 0:
            answer += 1

    return answer
    # answer = [k for k,v in cloth.items() if v > 0]
    # return len(answer)



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