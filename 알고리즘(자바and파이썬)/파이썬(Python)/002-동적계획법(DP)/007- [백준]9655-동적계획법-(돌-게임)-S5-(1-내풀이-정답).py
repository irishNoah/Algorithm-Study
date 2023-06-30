# [백준]9655-동적계획법-(돌-게임)-S5-(1-내풀이-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/9655

'''
* 제한 > 시간 : 1초 (기본 1초) / 메모리 : 128MB (기본 128MB)
- 1 ≤ N ≤ 1000 [N은 돌의 개수를 의미]

* 설계 [총 12분 소요] / 총 풀이 시간[총 13분 소요]
- N이 1~6일 때까지 차례대로 누가 이기는지 경우의 수를 구해보면
N이 짝수일 때는 창영(CY)이가, 홀수일 때는 상근(SK)이가 이기는 것을 알 수 있다.


'''
#============================================================

import sys

N = int(sys.stdin.readline().rstrip())

if N % 2 == 0:
    print("CY")
else:
    print("SK")