# [백준]2667-(단지번호붙이기)-(DFS&BFS)-S1-(1-내풀이-정답)-BFS&큐.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2667

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
그래프의 탐색 시작점을 모르기 때문에 전체를 돌면서 1인 지점에서 탐색을 시작합니다.
탐색 중 1인 부분은 0으로 바꿔 다시 방문하지 않도록 하고
한 번의 BFS가 끝나게 되면 더 이상 확장이 불가능 하므로 마을 하나가 탄생합니다.

이 마을안의 1의 개수들을 출력하면 되므로 다음 코드와 같이 count를 반환하면 됩니다.

*** 참고
> https://hongcoding.tistory.com/71

'''
#===================================================================================
# BFS & 큐(데크 라이브러리) 활용
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    n = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    cnt = 1 # 아파트 단지별 아파트 개수

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                cnt += 1
                queue.append((nx, ny))

    return cnt

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            result.append(bfs(graph, i, j))

result.sort()
print(len(result))
print(*result, sep='\n')



#===================================================================================