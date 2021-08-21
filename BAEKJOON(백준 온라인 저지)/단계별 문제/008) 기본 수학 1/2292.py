# 2292번 / 벌집 / B2 
# https://www.acmicpc.net/problem/2292

N = int(input()) # 찾아야 하는 값
first = 1 # 초기값
plus = 6 # 등차 값
room = 1 # 방

if N == 1: # 입력값이 1이면 방도 1이므로 1을 출력
    print(1)

else:
    while True:
        first = first + plus
        room+= 1
        if N <= first:
            print(room)
            break

        plus += 6
