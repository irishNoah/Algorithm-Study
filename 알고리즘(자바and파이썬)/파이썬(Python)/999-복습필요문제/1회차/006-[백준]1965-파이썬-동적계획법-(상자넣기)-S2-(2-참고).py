# [백준]1965-파이썬-동적계획법-(상자넣기)-S2-(2-참고).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1965

'''
참고 URL
https://alpyrithm.tistory.com/91

# 설명
- 상자를 입력받고 dp array를 1(해당 상자 1개)로 초기화해서 만든다.
- for문을 돌면서 주어진 상자 순서보다 앞에 있는 상자 중 크기가 작을 때 (상자의 수+1)과 비교해서 큰 값을 dp에 저장한다.
- dp 중 max인 값을 출력한다.
'''

n = int(input())

box = list(map, int(input().split()))

dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if box[i] > box[j]:
            dp[i] = max(dp[i], dp[j]+1)
            
print(max(dp))