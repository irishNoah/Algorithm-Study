# [백준]7562-(나이트의-이동)-(DFS&BFS)-S1-(1-참고풀이-정답)-bfs(큐).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/7562

'''
*** 제한 > 시간 : 1초 (기본 1초) / 메모리 : 256MB (기본 128MB)

*** 조건

*** 설계 [총 10분 소요] / 총 풀이 시간[총 50분 소요]
- 이동 횟수는 어떻게 구할 수 있으려낭???
- 그래프는 똑같이 0으로 채워 놓되, 이거는 최소 이동의 수를 물어보는 것이므로
이동할 때마다 이동된 좌표에 이동수 값을 넣어주면 된다.

1. BFS구현 최단경로
2. 이동 가능한 좌표를 dx, dy로 설정해준다.(8방향)
3. 한 번 이동한 좌표의 값에 +1씩 해주며 이동한다.(2번 이동하면, 그 좌표값은 +1+1=2가 된다.)
4. 도착지 좌표에 방문하면 그 좌표의 값을 return한다.

*** 참고
- https://velog.io/@falling_star3/%EB%B0%B1%EC%A4%80Python-7562%EB%B2%88-%EB%82%98%EC%9D%B4%ED%8A%B8%EC%9D%98-%EC%9D%B4%EB%8F%99
'''
#===================================================================================
### BFS(큐)
import sys
from collections import deque
input = sys.stdin.readline

# 나이트의 이동좌표 8개
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(x, y, endX, endY):
    queue = deque()
    queue.append([x,y])
    graph[x][y] = 0 ### graph의 좌표에 이동 수를 할당

    while queue:
        a, b = queue.popleft()

        ### 나이트가 도착점에 도착을 하면, 이동횟수를 리턴
        if a == endX and b == endY:
            return graph[a][b]

        ### 도착을 하지 않았다면, 이동 횟수를 계산
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]

            # 그래프 범위 내에 있으면 이동 횟수 증가
            if 0 <= nx < l and 0 <= ny < l:
                if graph[nx][ny] == 0: ## 만약, 0이 아닌 다른 수가 이미 있다면 최소 횟수에 어긋남
                    graph[nx][ny] = graph[a][b] + 1
                    queue.append([nx, ny])

tc = int(input())
while tc:

    l = int(input()) # 체스판 한 변의 길이
    graph = [[0]*l for _ in range(l)]
    # 시작점 좌표
    sX, sY = map(int, input().split())
    # 목표점 좌료
    tX, tY = map(int, input().split())

    if sX == tX and sY == tY:
        print(0)
        tc = tc-1
        continue

    answer = bfs(sX, sY, tX, tY)
    print(answer)
    tc = tc-1

#===================================================================================