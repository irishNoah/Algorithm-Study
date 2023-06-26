# [백준]2231-완전탐색-(분해합)-B3-(1-내풀이-런타임에러).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2231

'''
* 제한 > 시간 : 2초 / 메모리 : 192MB
- 시간 제한이 2초이기 때문에 탐색 문제일 가능성이 높다.
- 자연수 N(1 ≤ N ≤ 1,000,000)

* 설계
> 만약, 입력 n이 줄어들 때 분해합이 가능하려면 적어도
n의 자리수보다 분해합의 자리수는 최소 (n의 자리수 -1)이어야 한다.
- 즉, 입력값이 152이면 분해합은 최소 10의 자리부터 시작
> 따라서, for문을 "pow(10, len(str(n))-2)" 부터 수행한다.

* 결과
- IDE에서는 정답
- Python3와 pypy로 제출을 해도 런타임에러가 발생했다.

'''
#============================================================

import sys

n = int(sys.stdin.readline().rstrip())

leng = pow(10, len(str(n))-2)

res = -1


for cnt in range(leng, n+1):
    arr = list(map(str, str(cnt)))
    arr = list(map(int, arr))

    hap = cnt + sum(arr)

    if hap == n:
        res = cnt
        break

if res == -1:
    print(0)
else:
    print(res)