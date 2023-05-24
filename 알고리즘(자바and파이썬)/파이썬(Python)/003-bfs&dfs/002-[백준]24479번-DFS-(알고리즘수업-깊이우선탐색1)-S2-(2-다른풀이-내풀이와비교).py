# [백준]24479번-DFS-(알고리즘수업-깊이우선탐색1)-S2-(2-다른풀이-내풀이와비교)
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/24479

import sys
'''
재귀 최대 깊이 설정(특히, BFS와 DFS 사용시)을 해주어야 
런타임 에러를 방지할 수 있다.

만약, 이것을 설정 안할 경우 vs 코드 등에서는 맞게 출력이 되는데
코테 상에서는 런타임 에러가 발생할 수 있다.

*** 참고 URL >>> https://kingnamji.tistory.com/39
'''
sys.setrecursionlimit(10 ** 9) # 재귀 최대 깊이 설정
input = sys.stdin.readline

# -------------------------------------------------------

# 정점의 수 n, 간선의 수 m, 시작 정점 r 입력
n, m, r = map(int, input().split())

# 각 정점 순서대로 이어진 정점이 무엇이 있는지에 대한 정보를 담아둘 리스트 graph
graph = [[] for i in range(n+1)]

# 방문 했는지에 대한 여부를 파악하는 리스트 visited 생성
# visited = [False] * (m+1) # 내 풀이
visited = [0] * (n+1) # 다른 풀이

# 각 노드가 몇 번째로 방문을 했는지 파악하기 위한 변수 count
count = 1 # 다른 풀이(내 풀이에 아예 없었음)

for _ in range(m):
    # 간선 정보 a, b 입력
    a, b = map(int, input().split())

    # 각 노드의 정보를 담음
    graph[a].append(b)
    graph[b].append(a)

### 깊이 우선 탐색을 하기 위한 사용자 정의 함수 dfs
def dfs(v):
    '''
    # 전역 변수 count 사용
    # 전역 변수는 함수 밖보다는 안에서 gloabl 키워드를 활용해야 함
    # 참고 URL > https://www.infoking.site/64
    '''
    global count # 다른 풀이(내 풀이에 아예 없었음)

    ### 현재 노드에 대해서 방문한 순서(= count)를 visited[v]에 저장
    # visited[v] = True # 내 풀이
    visited[v] = count # 다른 풀이

    ### graph[v] 오름차순 배열 정렬
    graph[v].sort() # 다른 풀이(내 풀이에 아예 없었음)

    ### dfs 수행
    for i in graph[v]:
        if visited[i] == 0:
            count += 1
            dfs(i)


# 사용자 정의 함수 dfs 수행
dfs(r)

# 결과값 출력
for k in range(1, n+1):
    print(visited[k]) 

'''
*** 이번 문제의 특징
- bfs/dfs 기본 이론에서는 각 노드가 방문한 대로 바로 그 노드의 값을 출력했다.
- 이번 문제는 노드 방문 순서가 아니라, 각 노드가 차례대로 몇 번째 순서에 방문했는지를 구하는 것이었다.
- bfs/dfs 기본 이론에서는 visited 리스트의 값을 False로 세팅했다.
- 하지만, 이런 문제의 유형에서는 각 노드마다의 방문 순서값을 구하는 것이므로
visited의 각 값을 false가 아니라 정수 0으로 세팅하는 것이 좋다.

*** 새로 알게 된 점
1.  # 재귀 최대 깊이 설정
- sys.setrecursionlimit(10 ** 9) # 재귀 최대 깊이 설정
2. 전역 변수 활용
- 함수 밖에서는 선언만 해도 상관 없음
- 함수 안에서는 반드시 전역 변수 키워드 global을 활용해야 함!!!

*** 유의점
- 문제에서 n과 m이 동일한 수로 사용됐다고, 
프로그래밍에서 임의로 n과 m을 사용할 자리에 막 사용하지 말기!!!
- 이것 때문에, 코테 검사에서 문제가 틀리게 된다!!!
'''