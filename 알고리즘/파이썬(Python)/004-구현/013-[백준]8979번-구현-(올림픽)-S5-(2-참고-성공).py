# [백준]8979번-구현-(올림픽)-S5-(2-참고-성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/8979

'''
# 문제 풀이

1. 금-은-동 순으로 정렬까지 하는 것은 다랑 동일
2. 그 다음 등수를 알고자하는 국가번호가 정렬된 배열의 몇 번째 인덱스에 있는지 확인
3. 어차피 동일한 금-은-동 수라면 랭킹이 동일한 것이니, +1한 값을 출력

'''

import sys

input = sys.stdin.readline
n, k = map(int, input().split())

s = []

for i in range(n):
    s.append(list(map(int, input().split())))

s.sort(key=lambda x : (-x[1], -x[2], -x[3]))

# 국가번호의 index 찾기
for i in range(n):
    if s[i][0] == k:
        index = i
        break

# 정렬된 배열을 검사하며 국가번호 index의 금메달, 은메달, 동메달의 수와 같다면
# i에 1을 더한 값을 출력
for i in range(n):
    if s[index][1:] == s[i][1:]:
        print(i + 1)
        break