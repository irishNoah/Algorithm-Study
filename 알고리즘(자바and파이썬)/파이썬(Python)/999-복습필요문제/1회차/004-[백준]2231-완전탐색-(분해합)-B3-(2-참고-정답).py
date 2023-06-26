# [백준]2231-완전탐색-(분해합)-B3-(2-참고-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2231

'''
* 제한 > 시간 : 2초 / 메모리 : 192MB
- 시간 제한이 2초이기 때문에 탐색 문제일 가능성이 높다.
- 자연수 N(1 ≤ N ≤ 1,000,000)

* 내 풀이와 다른점
> 굳이, 자리수 따지지 않고 그냥 정직히 1부터 차례대로 구했다.
- 나도 애초에 이렇게 할 걸...

'''
#============================================================

import sys

n = int(sys.stdin.readline().rstrip())

for cnt in range(1, n+1):
    arr = sum(map(int, str(cnt)))

    hap = cnt + arr

    if hap == n:
        print(cnt)
        break
    if cnt == n:
        print(0)

