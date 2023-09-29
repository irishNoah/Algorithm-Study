# [백준]24479-(알고리즘 수업 - 깊이 우선 탐색 1)-(DFS)-S2-(5-내풀이-정답)-스택.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/24479

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 10분 소요] / 총 풀이 시간[총 34분 소요]
>>> 재귀는 근데, 시간 초과라고 뜨는뎅...???

*** 참고

'''
#===================================================================================

### 스택으로 문제 DFS 구현
import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)] # 각 노드의 연결 정보를 담은 리스트 graph

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드 연결 정보를 내림차순으로 정렬해줘야 스택을 pop() 진행 가능
for idx in range(1, len(graph)):
    graph[idx].sort(reverse=True)

visited = [-1] * (N+1) # 방문 여부
result = [0] * (N+1)

def DFS(start):
    stack = [start]
    cnt = 1 # 방문 순서 값

    while stack:
        cnt_node = stack.pop() # 스택 최상단 노드 추출

        if visited[cnt_node] == 1: # 방문 했었으면 다음 while문 진행
            continue

        ### 방문한 적 없다면
        visited[cnt_node] = 1 # 방문한 것으로 변경
        result[cnt_node] = cnt # 해당 노드가 몇 번째로 방문 됐는지 할당
        cnt += 1 # 방문 순서 값 증가

        for adjNode in graph[cnt_node]:
            if visited[adjNode] == -1:
                stack.append(adjNode)

    return result

DFS(R)
print(*result[1:], sep='\n')


#===================================================================================