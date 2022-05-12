# https://github.com/irishNoah/Algorithm-Study
# 1181번 / 단어 정렬하기 / S5
# https://www.acmicpc.net/problem/1181

import sys
input = sys.stdin.readline

N = int(input())

list_arr = []

while 1:
    # while문 종료 조건
    if N == 0:
        break

    # sys.stdin.readline()은 '\n\'를 포함하기 때문에
    # 입력을 연속으로 받는다면 에러가 발생할 수 있음
    # 이를 방지하게 위해 strip()을 사용해야 함
    list_arr.append(input().strip())

    N = N - 1

# 중복 제거를 위해 set() 사용
set_list_arr = set(list_arr)

# set 타입으로 되어 있는 set_list_arr를 list 타입으로 강제 변환 후
# list_arr에 할당
list_arr = list(set_list_arr)

# 단어 순으로 정렬
list_arr.sort()

# 그 이후 len 값을 통해 정렬
list_arr.sort(key = len)

for x in list_arr:
    print(x)