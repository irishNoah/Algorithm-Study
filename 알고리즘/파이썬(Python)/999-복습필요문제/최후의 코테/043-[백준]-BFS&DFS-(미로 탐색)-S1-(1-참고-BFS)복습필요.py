'''
043-[백준]-BFS&DFS-(미로 탐색)-S1-(1-참고-BFS)복습필요.py

### 주소
> https://www.acmicpc.net/problem/2178

### 참고
> 나동빈 이코테 책

16:24 ~ 16:37
### 설계 5분, 총 13분

'''
#===================================================================================

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# 상/하/좌/우
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

# BFS 수행 결과 출력력
print(bfs(0,0)) # 시작지점


#===================================================================================