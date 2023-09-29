# [백준]14719-구현-(빗물)-G5-(2-참고-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/14719

'''
# 문제 풀이

> 참고 URL : https://bio-info.tistory.com/188

* 핵심 논리
> 핵심은 각 블록에 대해서, 왼쪽과 오른쪽을 탐색해
두 방향 모두에서 더 높은 블록에 둘러 쌓여있으면 빗물이 고이는 것을 이용하는 것입니다.
자기를 둘러싼 왼쪽과 오른쪽 블록 중 더 낮을 블록까지 빗물이 고이는 것을 이용합니다.

* 풀이 코드
> H(높이)와 W(너비), blocks(각 열의 블록 개수)를 입력받고,
빗물이 고일양을 저장할 변수를 result=0으로 초기화해줍니다.

for 문을 도는데 맨 왼쪽 블록과 맨 오른쪽 블록은 빗물이 고일 수 없으므로 빼고 돕니다.
각 i 번째 블록에 대해서 왼쪽과 오른쪽을 모두 탐색해
각각 가장 높은 블록을 left_max와 right_max에 저장해 줍니다.

둘 중 더 작은 블록 까지만 빗물이 고이므로 min(left_max, right_max)를 해서 lower_one에 저장합니다.
현재 블록(blocks[i])보다 lower_one이 큰 경우, lower_one - blocks[i] 만큼의 빗물이 고이므로,
조건문으로 처리해 줍니다.

그렇게 각 블록에서 계산된 빗물이 고인양을 모두 result에 더해줘서 출력하면 됩니다.

'''

import sys

H, W = [*map(int, sys.stdin.readline().split())]
blocks = [*map(int, sys.stdin.readline().split())]
result = 0  # 빗물의 고인 양

for i in range(1, W - 1):  # 맨 왼쪽과 맨 오른쪽은 고일 수 없다.
    left_max = max(blocks[:i])  # 왼쪽에서 제일 높은 블록
    right_max = max(blocks[i + 1:])  # 오른쪽에서 제일 높은 블록

    lower_one = min(left_max, right_max)  # 그중 가장 낮은 블록

    if blocks[i] < lower_one:  # 현재 블록이 lower_one 블록 보다는 낮아야 빗물이 고인다.
        result += lower_one - blocks[i]

print(result)