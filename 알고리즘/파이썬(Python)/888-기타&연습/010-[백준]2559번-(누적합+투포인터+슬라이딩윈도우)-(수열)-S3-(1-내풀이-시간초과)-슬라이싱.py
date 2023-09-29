# [백준]2559번-(누적합+투포인터+슬라이딩윈도우)-(수열)-S3-(1-내풀이-시간초과)-슬라이싱.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2559

'''
*** 제한 > 시간 : ?초 (기본 1초) / 메모리 : ?MB (기본 128MB)

*** 조건

*** 설계 [총 5분 소요] / 총 풀이 시간[총 22분 소요]
- n의 범위가 십만까지이기 때문에
O(N log N)이하의 시간 복잡도를 구성하고자
for문을 1번 사용했음에도 틀렸다.

'''
#===================================================================================

import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
# print(arr)

find = []
for i in range(0, len(arr)-k+1):
    val = sum(arr[i:i+k])
    find.append(val)

# print("find = ", find)
print(max(find))

#===================================================================================

### 예제 입력 1
# 10 2
# 3 -2 -4 -9 0 3 7 13 8 -3

### 예제 출력 1
# 21

### 예제 입력 2
# 10 5
# 10 5

### 예제 출력 2
# 31