# [백준]1018-완전탐색-(체스판-다시-칠하기)-S4-(2-참고).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1018

'''
* 제한 > 시간 : 2초 / 메모리 : 128MB
- 제한시간 2초
- N(가로), M(세로)의 범위 >>> 8 <= N & M <= 50

* 설계 [총 15분 소요] / 총 풀이 시간[총 분 소요]

* 다른 점
- 우선, for문을 통해 시작점과 종료점 값을 아주 간단히 구한이후
8*8을 구한 게 간단해 보였다.

'''
#============================================================

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

        # 'W'로 시작할 경우와 'B'로 시작할 경우 바뀐 체스판의 수 중 작은 수를 count 리스트에 더해준다.
        count.append(min(index1, index2))

# 모든 경우의 수를 다 체크한 후, count 중 제일 작은 수를 출력하고 프로그램을 종료한다.
print(min(count))