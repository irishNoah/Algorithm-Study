# https://github.com/irishNoah/Algorithm-Study
# 11650번 / 좌표 정렬하기 / S5
# https://www.acmicpc.net/problem/11650

N = int(input())

list_arr = []

while 1:
    if N == 0:
        break

    list_arr.append(list(map(int, input().split())))

    N = N - 1

# 파이썬은 2차원 정렬역시 sorted()를 통해서 구현할 수 있다.
list_arr = sorted(list_arr)

for i in range(0, len(list_arr)):
    print("{0} {1}".format(list_arr[i][0], list_arr[i][1]))