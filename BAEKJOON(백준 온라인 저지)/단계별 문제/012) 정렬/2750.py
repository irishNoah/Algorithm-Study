# 2750번 / 수 정렬하기 / B1
# https://www.acmicpc.net/problem/2750

N = int(input())

arr = []

for i in range (0, N) :
    value = int(input())
    arr.append(value)

arr.sort()

for i in range (0, N) :
    print(arr[i])