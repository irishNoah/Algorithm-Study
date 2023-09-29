# [백준]1012-(유기농-배추)-(DFS&BFS)-S2-(1-내풀이-정답)-bfs(큐).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1012

'''
*** 제한 > 시간 : 1초 (기본 1초) / 메모리 : 512MB (기본 128MB)

*** 조건

*** 설계 [총 8분 소요] / 총 풀이 시간[총 50분 소요]
- 이거는 이전에 풀었던 백준 2667번 "아파트단지 붙아기"와 비슷
- 2667번은 각 단지마다 몇 개의 아파트가 있느냐였는데, 1012번 같은 경우
카운트 된 아파트 단지가 몇 개인지 len()으로 출력해주면 된다.
- bfs로 푼다.
>>>>>>>>>>>>>>> []가 아닌, () 임에 유의를 해야 함

*** 참고

'''
#===================================================================================
### DFS(그래프-재귀) & BFS(그래프-큐)
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9) # 필요없기는 함 ㅎ

T = int(input()) # 테스트 케이스의 수

while T > 0:
    T = T-1 # while문 종료 조건

    M, N, K = map(int, input().split()) # M이 가로, N이 세로임에 유의

    # 농장의 배추 정보 생성
    graph = [[0 for _ in range(N)] for _ in range (M)]
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a][b] = 1

    # 상,하,좌,우
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def bfs(graph, a, b):
        queue = deque()
        queue.append((a,b)) # []가 아닌, () 임에 유의를 해야 함
        graph[a][b] = 0
        cnt = 1 # 벌레 마리 수

        while queue:
            x, y = queue.popleft()

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or nx >= M or ny < 0 or ny >= N:
                    continue

                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    cnt += 1
                    queue.append((nx, ny))

        return cnt

    # 각 배추 구간마다 배추가 몇 개있는지 카운트
    result = []
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                result.append(bfs(graph, i, j))

    print(len(result)) # 배추 구간 = 마리수 필요
#===================================================================================