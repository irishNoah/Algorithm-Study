# [백준]1051-(숫자-정사각형)-(구현)-S3-(2-참고-).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1051

'''
*** 제한 > 시간 : 2초 (기본 1초) / 메모리 : 128MB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]

*** 참고
- https://velog.io/@dy6578ekdbs/1051%EB%B2%88-%EC%88%AB%EC%9E%90-%EC%A0%95%EC%82%AC%EA%B0%81%ED%98%95-python

'''
#===================================================================================

def find_squre(s):
    for i in range(N-s+1): # 행
        for j in range(M-s+1): # 열
            if numbers[i][j] == numbers[i][j+s-1] == numbers[i+s-1][j] == numbers[i+s-1][j+s-1]:
                return True

    return False


N, M = map(int, input().split())
numbers = [list(map(int, list(input()))) for _ in range(N)]

size = min(N,M)

# 최대 크기부터 하나씩 줄여가며 시작
for k in range(size, 0, -1):
    # 네 꼭지점의 크기가 같은 정사각형을 찾았으면 True를 받아 넓이를 출력해주고 break
    if find_squre(k) == True:
        print(k**2)
        break

#===================================================================================