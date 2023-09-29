# [백준]1697-(숨바꼭질)-(DFS&BFS)-S1-(1-내풀이-메모리초과)-bfs.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1697

'''
*** 제한 > 시간 : 1초 (기본 1초) / 메모리 : 256MB (기본 128MB)

*** 조건

*** 설계 [총 5분 소요] / 총 풀이 시간[총 21분 소요]


*** 참고

'''
#===================================================================================
### 그래프 & bfs
import sys
from collections import deque
input = sys.stdin.readline

# N은 수빈이가 있는 위치, K는 동생이 있는 위치
N, K = map(int, input().split())
# cnt = 0 # 수빈이가 동생을 찾는 가장 빠른 시간

def bfs(N):
    queue = deque()
    queue.append(N)
    cnt = 0 # 수빈이가 동생을 찾는 가장 빠른 시간

    while queue:
        # 계산을 진행하고자 하는 값
        node = queue.popleft()
        minus = node-1
        mul = node*2

        # 계산한 값이 K와 같다면 리턴
        if minus == K or mul == K:
            return cnt

        queue.append(minus); queue.append(mul)
        cnt += 2

    # cnt += 1 # 시간 1 증가

answer = bfs(N)
time = 0
while True:
    if answer // 2 > 0:
        answer = answer // 2
        time += 1

    else:
        break

print(time)

#===================================================================================