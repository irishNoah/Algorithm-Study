# [백준]2606-(바이러스)-(DFS&BFS)-S2-(1-내풀이-정답)-BFS&큐.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2606

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 10분 소요]
- 인접 노드는 내림차순으로 진행한다.

*** 참고

'''
#===================================================================================
# BFS & 큐(데크 라이브러리) 활용
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

computer = int(input().rstrip())
line = int(input().rstrip())

graph = [[] for _ in range(computer+1)]
visited = [-1] * (computer+1)
for _ in range(line):
    a, b= map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for idx in range(1, computer+1):
    graph[idx].sort()

def bfs(start):
    cnt = 0 # 감염된 컴퓨터의 수
    queue = deque([start])
    visited[start] = 1

    while queue:
        node = queue.popleft()

        for adjNode in graph[node]:
            if visited[adjNode] == -1:
                visited[adjNode] = 1
                queue.append(adjNode)
                cnt += 1

    return cnt

print(bfs(1)) # 1번 컴퓨터부터 시작

#===================================================================================