# [백준]2667-(단지번호붙이기)-(DFS&BFS)-S3-(2-다른풀이-참고)-BFS&재귀.py
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
### dfs & 재귀
import sys
input = sys.stdin.readline

N = int(input().rstrip()) # 정사각형 한 변의 길이 입력

graph = []
result = []
count = 0 # 여기서 global을 사용하지는 않지만, 이게 없으면 컴파일 에러 발생

# 정사각형 그래프 할당
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

# 상 / 하 / 좌 / 우
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x, y):
    global count # 동일 단지수의 아파트 개수

    # 정사각형 범위를 벗어나는 것에 대한 예외 처리
    if x < 0 or x >= N or y < 0 or y >= N:
        return

    if graph[x][y] == 1:
        count += 1 # 동일 단지수의 아파트 개수 1 증가
        graph[x][y] = 0 # 0으로 초기화 해야 주변 아파트에서 중복 카운트하지 않아

        # 각 그래프의 x,y 기준으로 상하좌우를 돌면서 재귀 수행
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

# 그래프의 원소가 1인 경우에만 dfs 수행
for i in range(N):
    for j in range(N):
        # 초기 그래프에서 연결된 놈들이 0이 되면 해당 아파트 단지의 탐색을 끝내고,
        # 아파트 단지의 아파트 수를 result 리스트에 할당
        if graph[i][j] == 1:
            dfs(i, j)
            result.append(count)
            count = 0 # 단지의 아파트 수 0으로 초기화

result.sort()

print(len(result))
print(*result, sep='\n')

#===================================================================================