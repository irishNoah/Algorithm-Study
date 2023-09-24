'''
016-[프로그래머스]-구현-(체육복)-LV1-(1-내풀이).py

### 주소
> https://school.programmers.co.kr/learn/courses/30/lessons/42862

### 설계 7분, 총 34분

'''

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