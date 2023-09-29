# [백준]1205-구현-(등수-구하기)-S4-(2-참고-성공).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1205

'''
# 문제 풀이

* 참고 URL
> https://alpyrithm.tistory.com/68

1. 0 <= n <= p이고 둘째 줄은 n이 0보다 큰 경우에만 주어지므로 n == 0일 때와 n > 0인 경우로 나눈다.
2. n == 0이면 10 <= p <= 50이므로 랭킹은 1이 된다.
3. n > 0인 경우
> n == p이면서 랭킹 중 가장 작은 점수가 새로운 점수보다 크거나 같다면 -1을 출력한다.
> 그 외의 경우 랭킹 점수를 for문으로 돌면서 랭킹의 점수가 새로운 점수보다 작거나 같으면 그 등수가 새로운 점수의 등수가 된다.
> for문을 돌았지만 새로운 점수보다 작거나 같은 점수가 없다면 n+1이 새로운 점수가 된다.

*** 중복된 점수는 계산 안하나?
- 어차피, 예제2번과 4번을 건너 뛰면 어차피 범위 내에서 랭킹을 구하는 것
- score[i] <= new일 경우에만 res값이 바뀌는 것이니까 중복된 점수는 계산할 필요가 없다

'''

import sys

n, new, p = map(int, input().split())

if n == 0: # 예제 입력 4번에 해당
    print(1)

else:
    score = list(map(int, sys.stdin.readline().split()))

    if n == p and score[-1] >= new: # 예제 입력 2번에 해당
        print(-1)

    else:
        res = n+1
        for i in range(n):
            if score[i] <= new:
                res = i+1
                break

        print(res)