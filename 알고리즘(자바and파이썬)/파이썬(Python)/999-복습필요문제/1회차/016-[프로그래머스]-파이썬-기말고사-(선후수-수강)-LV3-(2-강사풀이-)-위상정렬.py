# [프로그래머스]-파이썬-기말고사-(선후수-수강)-LV3-(2-강사풀이-)-위상정렬.py
# https://github.com/irishNoah/Algorithm-Study

'''
*** 제한 > 시간 : 10초 (기본 1초) / 메모리 : 2GB (기본 128MB)

*** 조건

*** 설계 [총 -분 소요] / 총 풀이 시간[총 -분 소요]
기본적인 위상정렬 문제입니다. 위상정렬이 기본적인 알고리즘은 아니지만 말이죠. 기본적인 흐름은 다음과 같습니다.
1.선수과목이 없는/모두 수강된 과목(leaf)을 모두 구한다.
2. 가장 작은 Leaf를 수강한다. 새로 모두 수강된 과목이 있으면 leaf에 추가한다.
3. 1-2를 계속 반복하면 된다.

위상정렬에 대한 자세한 내용은 다음을 참조하시면 됩니다.

*** 참고
> 위상정렬
- https://velog.io/@kimdukbae/%EC%9C%84%EC%83%81-%EC%A0%95%EB%A0%AC-Topological-Sorting

'''
#===================================================================================

from heapq import heappush, heappop
from collections import defaultdict


def solution(s1, s2, k):
    # 전체 그래프 생성
    graph = defaultdict(list)
    for X, Y in zip(s1, s2):
        graph[Y].append(X)

    answer, leafs = [], []

    # K에 관련된 그래프 생성
    stack = [k]
    visited = set([k])
    graph_k = defaultdict(list)
    indegrees = defaultdict(int)
    while stack:
        node = stack.pop()
        if graph[node]:
            for prev in graph[node]:
                indegrees[node] += 1
                graph_k[prev].append(node)
                if prev not in visited:
                    stack.append(prev)
                    visited.add(prev)
        else:
            heappush(leafs, node)

    # 위상정렬
    while leafs:
        node = heappop(leafs)
        answer.append(node)
        for next_node in graph_k[node]:
            indegrees[next_node] -= 1
            if not indegrees[next_node]:
                heappush(leafs, next_node)

    return answer

#===================================================================================

# 예제 1
s1 = ["A", "E", "B", "D", "B", "H", "F", "H", "C"]
s2 = ["G", "C", "G", "F", "J", "E", "B", "F", "B"]
k = "B"
print(solution(s1, s2, k)) # ["D", "H", "E", "C", "F", "B"]

# 예제 2
candy = ["A", "E", "B", "D", "B", "H", "F", "H", "C"]
positions = ["G", "C", "G", "F", "J", "E", "B", "F", "B"]
k = "G"
print(solution(s1, s2, k)) # ["A", "D", "H", "E", "C", "F", "B", "G"]


# def solution(candy, positions):
#     answer = []
#     return answer