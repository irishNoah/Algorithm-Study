# https://github.com/irishNoah/Algorithm-Study
# 11650번 / 좌표 정렬하기(2) / S5
# https://www.acmicpc.net/problem/11650

# 해당 문제 풀이는 lamda를 이용하여 해결하였음
# 참고 : https://haesoo9410.tistory.com/193

N = int(input())

list_arr = []

while 1:
    if N == 0:
        break

    list_arr.append(list(map(int, input().split())))

    N = N - 1

# lamda를 이용
list_arr.sort(key=lambda x:(x[0], x[1]))

for i in range(0, len(list_arr)):
    print("{0} {1}".format(list_arr[i][0], list_arr[i][1]))