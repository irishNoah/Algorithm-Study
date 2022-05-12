# https://github.com/irishNoah/Algorithm-Study
# 1026번 / 보물 / S4
# https://www.acmicpc.net/problem/1026

import sys

n = int(input()) # 길이 입력

# list_A, list_B 공백으로 구분하여 입력
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

# 만약 list_A, list_B의 길이가 n과 다를 경우 시스템 강제 종료
if len(list_A) != n or len(list_B) != n:
    print("len error!!!")
    sys.exit()

list_A.sort() # list_A 오름차순 정렬

sum = 0 # 최소값을 구하기 위한 변수 sum

while 1:
    if n == 0: # while문 탈출 조건
        break

    # list_B에서 최대값을 찾은 후 max_B_value에 대입
    max_B_value = max(list_B)

    # list_B 요소 중 최대값과 list_A의 최소값을 더한 후 sum에 덧셈으로 할당
    # 자고로 list_A의 최소값은 list_A[0]과 동일한 값임
    sum += max_B_value * list_A[0]

    list_A.pop(0) # list_A에서 0번째 인덱스 값 제거

    # list_B에서 max_B_value값을 가지고 있는 리스트 요소 제거
    # list_B에서 동일한 값을 갖고 있는 요소가 여러 개여도
    # remove()는 가장 먼저 찾는 값만 제거하기 때문에 문제 없음
    list_B.remove(max_B_value) 

    n = n-1 # n은 1 감소

print(sum)