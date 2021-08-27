# 2606 / 바이러스 / S3
# https://www.acmicpc.net/problem/2606

# 컴퓨터 대수 N
N = int(input())
# 간선의 개수 M 
M = int(input())

# 행렬 방식으로 하기 위해 2차원 행렬 생성
graph = [[] * (N+1) for _ in range(N+1)]

for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0] * (N+1)

# 깊이 우선 탐색 dfs 구현 함수
def dfs(start):
    # discoverd = []
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            # 재귀 함수
            dfs(i)
            cnt += 1
            
dfs(1)
# 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수 출력
print(cnt)