# https://github.com/irishNoah/Algorithm-Study
# 1094번 / 막대기 / S5
# https://www.acmicpc.net/problem/1094

import sys

x = int(input()) # 원하는 막대기의 길이

cnt = 0 # 막대의 개수

# 만약 입력한 x가 1일 경우 바로 1 출력
if x == 1: 
    cnt = 1
    print(cnt)
    sys.exit() # 파이썬 강제 종료, 즉 이후 코드는 실행 x

# 입력한 x가 1보다 큰 경우에 아래의 코드들 실행
stick = [64, 32, 16, 8, 4, 2, 1]

i = 0 # stick의 인덱스로 들어갈 i, i는 0으로 초기화

# x가 0이 될 때까지 while문 실행
while 1:
    # stick[i]가 x보다 클 경우 i를 1 증가시킨 후 continue 실행
    if  stick[i] > x :
        i += 1
        continue

    # stick[i]가 x보다 작거나 같을 경우 x에서 stick[i]를 뺀 값을 x에 대입한 이후
    # cnt는 1 증가
    x = x - stick[i]
    cnt += 1

    if x == 0: # while문 탈출
        break  

print(cnt) # cnt 출력