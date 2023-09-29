# [백준]1018-완전탐색-(체스판-다시-칠하기)-S4-(2-내풀이-복습참고).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1018

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 13분 소요] / 총 풀이 시간[총 ???분 소요]
- 코드 설명 참고할 것

*** 참고

'''
#===================================================================================
N, M = map(int, input().split())
original = []
count = []

for _ in range(N):
    original.append(input())

for a in range(N-7): # a는 행에 대하여 원래의 체스 판에서 8*8로 자를 수 있는 범위의 시작점
    for b in range(M-7): # b는 열에 대하여 원래의 체스 판에서 8*8로 자를 수 있는 범위의 시작점

        index1 = 0 # 'W'로 시작할 경우 바뀐 체스 판의 갯수
        index2 = 0 # 'B'로 시작할 경우 바뀐 체스 판의 갯수

        # 행과 열의 시작점 a, b를 기준으로 8칸씩 모두 체크
        for i in range(a, a+8):
            # 현재 행의 번호 i, 현재 열의 번호 j의 합이 짝수이면 시작점의 색깔과 같아야 함
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if original[i][j] != 'W':
                        index1 += 1
                    if original[i][j] != 'B':
                        index2 += 1

                # 현재 행의 번호 i, 현재 열의 번호 j의 합이 홀수이면 시작점의 색깔과 달라야 함
                else:
                    if original[i][j] != 'B':
                        index1 += 1
                    if original[i][j] != 'W':
                        index2 += 1

        # print(index1, index2) # 예제 1번과 같은 경우 index1은 1, index2는 63

        # 'W'로 시작할 경우와 'B'로 시작할 경우 바뀐 체스판의 수 중 작은 수를 count 리스트에 더해준다.
        count.append(min(index1, index2))

# 모든 경우의 수를 다 체크한 후, count 중 제일 작은 수를 출력하고 프로그램을 종료한다.
print(min(count))


#===================================================================================