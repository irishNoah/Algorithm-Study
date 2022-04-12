# https://github.com/irishNoah/Algorithm-Study
# 11651번 / 좌표 정렬하기 2 / S5
# https://www.acmicpc.net/problem/11651

# 해당 문제 풀이는 lamda를 이용하여 해결하였음
# 참고 : https://haesoo9410.tistory.com/193

import sys
sys = sys.stdin.readline

N = int(input())

list_arr = []

while 1:
    if N == 0:
        break

    list_arr.append(list(map(int, input().split())))

    N = N - 1

# lamda를 이용
#  좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬
list_arr.sort(key=lambda x:(x[1], x[0]))


for x, y in list_arr:
    print(x, y)