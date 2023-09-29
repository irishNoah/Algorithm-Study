# [백준]2667-(단지번호붙이기)-(DFS&BFS)-S3-(1-내풀이-참고)-BFS&재귀.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2667

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]

*** 참고
> https://ji-gwang.tistory.com/294
- bfs 방식으로도 풀이가 있음!!!


'''
#===================================================================================

# DFS & 재귀 활용하여 풀이
import sys
input = sys.stdin.readline

N = int(input().rstrip()) # 정사각형 변의 길이 입력

# 정사각형의 정보 입력
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

result = [] # 아파트 단지 리스트
count = 0 # 단지마다 몇 개의 아파트로 구성되어 있는지에 대한 변수

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    # print(1)
    global count # 전역변수 count

    # 그래프 범위 초과에 대한 예외 처리
    if x < 0 or x >= N or y < 0 or y >= N:
        return

    if graph[x][y] == 1:
        graph[x][y] = 0
        count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)


# x, y를 이동하며 값이 1인 경우에만 dfs 수행
for i in range(N):
    for j in range(N):
        # 아래 if문을 수행하면 한 번의 dfs마다 한 아파트 단지를 다 탐색
        if graph[i][j] == 1:
            dfs(i, j) # 아파트 단지 탐색 수행
            result.append(count) # 아파트 단지의 아파트 개수 할당
            count = 0 # 전역 변수 count를 0으로 초기화

result.sort() # 아파트 단지의 개수를 오름차순 정렬
print(len(result))
print(*result, sep='\n')












#===================================================================================