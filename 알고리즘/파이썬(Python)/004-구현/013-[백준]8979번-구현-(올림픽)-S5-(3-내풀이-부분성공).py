# [백준]8979번-구현-(올림픽)-S5-(3-내풀이-부분성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/8979

'''
# 문제 풀이

1. 참고해서 풀이했던 것과 유사
2. 단, 나는 arr의 [i][1:]과 [i-1][1:] 값을 계속 비교하며
rank += 1을 해주었다.
그리고 arr[i][0] == K(찾고자 하는 국가 번호) 가 된다면
그 때 rank를 출력하도록 짜주었다.

>>> 왜 부분 점수를 맞았을까?
- 개인적인 생각이지만, 만약 공동등수가 100개 있다고 가정했을 때
내가 찾고자 하는 국가번호가 리스트 안에서 공동등수 중 마지막에 있을 경우
비효율적일 것이다.
- 왜냐하면, 공동등수에서 1번째 위치하는 것이나 100번째 위치하는 것이나
등수는 동일하니까!

>>> 그럼 어떻게 개선하면 될까?
- 참고했던 것처럼, 먼저 국가번호가 리스트 안에서의 인덱스가 어디인지 확인하고
이 인덱스의 값과 공동등수 중 첫 번째에 위치한 값이 동일한 경우 그 등수를 출력하게 하면 되지 않을까?

'''
#============================================================

import sys

N, K = map(int, sys.stdin.readline().split())

nara = []
for _ in range(N):
    nara.append(list(map(int, sys.stdin.readline().split())))

arr = sorted(nara, key= lambda x: (-x[1], -x[2], -x[3]))

rank = 1
for i in range(1, N):
    if arr[i][1:] != arr[i-1][1:]:
        rank += 1

    if arr[i][0] == K:
        print(rank)
        break