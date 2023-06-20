# [백준]2852-구현-(NBA-농구)-S3-(1-내풀이-실패).py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2852

'''
# 문제 풀이

> 제발 str 타입으로 받았는지 아닌지 확인 좀 하자
> 에러 : TypeError: can only concatenate str (not "int") to str
- 참고 URL : https://seongsu-minki.tistory.com/21

1. 부호 값을 통해서 접근한 방식은 좋았던 것 같다.
2. 초 계산이 어려울 뿐 ㅎㅎ...
'''
#============================================================

# import sys

case = int(input())

game = 48*60 # 총 시간을 초 단위로 전환

check = 0 # 1팀이 이기고 있으면 양수, 2팀이 이기고 있으면 음수, 비기고 있으면 0
oneSec = 0; twoSec = 0

for _ in range(case):
    num, time = input().split()
    min = int(time[:2]); sec = int(time[3:])

    if check == 0: # 비기고 있던 경우
        if num == "1":
            check += 1
            oneSec = oneSec + (game - (min*60+sec))
        if num == "2":
            check -= 1
            twoSec = twoSec + (game - (min*60+sec))

    if check > 0: # 1팀이 이기고 있던 경우
        if num == "1":
            check += 1
        if num == "2":
            check -= 1

        if check == 0:
            oneSec = oneSec - (game - (min*60+sec))

    if check < 0:  # 2팀이 이기고 있던 경우
        if num == "2":
            check -= 1
        if num == "1":
            check += 1

        if check == 0:
            twoSec = twoSec - (game - (min * 60 + sec))

print(oneSec, twoSec)