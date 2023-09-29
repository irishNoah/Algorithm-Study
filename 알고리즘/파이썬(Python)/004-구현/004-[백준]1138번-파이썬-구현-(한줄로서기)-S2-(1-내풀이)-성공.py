# [백준]1138번-파이썬-구현-(한줄로서기)-S2-(1-내풀이)-성공.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1138

'''
문제 생각하는데 20분
코드하는데 10분
'''

# 사람수
n = int(input())

# 각 키(1~n) 인원마다 왼쪽에 몇 명에 있는지에 대한 정보를 배열 arr에 담음
arr = list(map(int, input().split()))

# 0으로만 이루어진 table 배열 생성 > 0의 개수로 왼쪽에 있는 사람 수 파악하려고
table = [0] * n


for i in range(0, n):
    # 각 키 인원 왼쪽에 있는 사람 수
    left = arr[i]

    cnt = 0

    for j in range(0, n):
        if left == cnt:
            if table[j] == 0:
                # 해당 테이블에 키 정보 할당
                table[j] = i+1
                break

            else:
                continue

        # 각 키마다 왼쪽에 몇 명 들어오는지 체크
        if table[j] == 0:
            cnt += 1

print(*table)