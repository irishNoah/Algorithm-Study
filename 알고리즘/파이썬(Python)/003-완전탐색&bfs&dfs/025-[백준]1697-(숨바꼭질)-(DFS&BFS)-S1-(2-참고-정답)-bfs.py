# [백준]1697-(숨바꼭질)-(DFS&BFS)-S1-(2-참고-정답)-bfs.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1697

'''
*** 제한 > 시간 : 1초 (기본 1초) / 메모리 : 256MB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
- 몇 초 == 이동 거리
- 해당 문제와 같은 경우 동생의 위치를 도대체 어느 정도까지 해야 찾을 수 있을까는 모르기 때문에
리스트가 상당히 길어질 수 있다. 이것에 대한 제한을 둬야 메모리 초과를 받지 않을 수 있다.

*** 참고
- https://wook-2124.tistory.com/273
'''
#===================================================================================
### 그래프 & bfs
import sys
from collections import deque

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k: # 같으면, 초 출력
            return array[v]
        for next_v in (v-1, v+1, 2*v): # 거리 -1, +1, *2 중에
            # 범위 내에 있으면서, 아직 값이 0인거면
            if 0 <= next_v < MAX and not array[next_v]:
                array[next_v] = array[v] + 1
                q.append(next_v)


MAX = 100001        # 시간초과 안나게 수 제한
array = [0] * MAX   # 이동하는 거리를 알기 위한 변수
n, k = map(int, sys.stdin.readline().split())
print(bfs(n))

#===================================================================================