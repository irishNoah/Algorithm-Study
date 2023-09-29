# [백준]1205-구현-(등수-구하기)-S4-(1-내풀이-성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1205

'''
# 문제 풀이

1. 저번 풀이보다 나아졌다.
'''
#============================================================

import sys

# 0 <= N <= P /// 10 <= P <= 50
N, new, P = map(int, sys.stdin.readline().split())

# 리스트 길이가 0이면 어차피 1등
if N == 0:
    print(1)
    sys.exit(0)

arr = list(map(int, sys.stdin.readline().split()))

# arr의 마지막 값이 새로운 점수 이상인 상황에서, N == P이면
# 랭킹 리스트에 들어갈 수 없으므로 -1 리턴
if arr[-1] >= new and N == P:
    print(-1)
    sys.exit(0)


# 여기 위까지는 동일했음 ========================================

idx = N+1 # new가 가장 낮은 점수이면서, 동일한 것이 없을 때
for i in range(N): # 그 외의 경우
    if arr[i] <= new:
        idx = i+1
        break

print(idx)