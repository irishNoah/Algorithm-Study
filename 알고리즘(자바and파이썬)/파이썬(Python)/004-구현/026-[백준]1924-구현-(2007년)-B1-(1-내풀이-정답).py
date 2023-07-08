# [백준]1924-구현-(2007년)-B1-(1-내풀이-정답).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1924

'''
*** 참고 URL

*** 시간 : 2초 (기본 1초) / 메모리 : 128MB (기본 128MB)

*** 조건


*** 설계 [ 5분 소요] / 총 풀이 시간[총 12분 소요]
- 각 월의 날을 담은 리스트 days 생성 후, 각 월마다 있는 날짜 수를 할당
- 입력 월, 일에 맞게 날짜수를 계산해서 7로 나눈 나머지를 구한다.
    - 월:1, 화:2 ~~~ 토:6, 일:0
        - 날에 맞게 출력

'''
#============================================================

import sys

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month, day = map(int, input().split())

# 총 날짜수 계산
sumDay = 0
for i in range(0, month):
    if i == month-1:
        sumDay += day

    else:
        sumDay += days[i]

if sumDay % 7 == 1:
    print("MON")
elif sumDay % 7 == 2:
    print("TUE")
elif sumDay % 7 == 3:
    print("WED")
elif sumDay % 7 == 4:
    print("THU")
elif sumDay % 7 == 5:
    print("FRI")
elif sumDay % 7 == 6:
    print("SAT")
elif sumDay % 7 == 0:
    print("SUN")