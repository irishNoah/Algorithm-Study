# [프로그래머스]-파이썬-기말고사-(판데믹)-LV2-(2-강사풀이-)-DFS.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
- 스택을 이용한 재귀 알고리즘 DFS 활용

*** 참고

'''
#===================================================================================

def solution(rows, columns, max_virus, queries):
    grid = [[0] * columns for _ in range(rows)]

    def action(i, j):
        stack = [(i, j)]
        visited = set([(i, j)])
        while stack:
            i, j = stack.pop()
            if grid[i][j] < max_virus:
                grid[i][j] += 1
            else:
                for _i, _j in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                    if 0 <= _i < rows and 0 <= _j < columns and (_i, _j) not in visited:
                        visited.add((_i, _j))
                        stack.append((_i, _j))

    for i, j in queries:
        action(i - 1, j - 1)

    return grid

#===================================================================================

# 예제 1
rows = 3
columns = 4
max_virus = 2
queries = [[3,2],[3,2],[2,2],[3,2],[1,4],[3,2],[2,3],[3,1]]
print(solution(rows, columns, max_virus, queries)) # [[0,2,1,1],[2,2,2,1],[2,2,2,1]]
