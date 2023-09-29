# [현대소프티어]-파이썬-(근무시간)-LV1-(내풀이-성공)-문자열슬라이싱.py
# https://softeer.ai/practice/info.do?idx=1&eid=990

import sys

# 하루 근무 시간 계산하는 함수
def getTime(start, finish):
    start_hour = int(start[:2])
    start_min = int(start[3:])
    finish_hour = int(finish[:2])
    finish_min = int(finish[3:])

    # 하루 일하는 시간
    workTime = (60*finish_hour + finish_min) - (60*start_hour + start_min)
    
    return workTime


day = 5
sumTime = 0
while day != 0:

    start, finish = map(str, sys.stdin.readline().rstrip().split())
    sumTime += getTime(start, finish)

    day -= 1

print(sumTime)