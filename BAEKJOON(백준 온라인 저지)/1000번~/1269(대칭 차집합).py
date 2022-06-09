# https://github.com/irishNoah/Algorithm-Study
# 1269번 / 대칭 차집합 / S3
# https://www.acmicpc.net/problem/1269

import sys

# 집합 A,B의 각 원소의 개수에 해당되는 a,b 입력
a, b = map(int, input().split())

set_A = set(map(int, input().split())) # 집합 A 입력
set_B = set(map(int, input().split())) # 집합 B 입력

# 집합 A의 길이가 a와 다를 경우 시스템 강제 종료
if len(set_A) != a:
    print("error_A")
    sys.exit()

# 집합 B의 길이가 b와 다를 경우 시스템 강제 종료
if len(set_B) != b:
    print("error_B")
    sys.exit()

# 대칭 차집합 구하기
minus_A_B = set_A - set_B
minus_B_A = set_B - set_A

# 대칭 차집합의 원소의 개수 구하기
cnt = len(minus_A_B) + len(minus_B_A)
# 대칭 차집합의 원소의 개수 출력하기
print(cnt)