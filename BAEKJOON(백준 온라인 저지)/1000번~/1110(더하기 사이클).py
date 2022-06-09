# https://github.com/irishNoah/Algorithm-Study
# 1110번 / 더하기 사이클 / B1
# https://www.acmicpc.net/problem/1110

# num 입력
num = int(input())

# mok과 rest를 각각 -1로 초기화
mok = -1
rest = -1

# 입력된 num이 0~9 사이의 수일 경우
if num >= 0 and num <= 9:
    mok = int(0)
    rest = num

# 입력된 num이 10 이상의 수일 경우
else:
    mok = num // 10
    rest = num % 10

cnt = 0 # 사이클의 길이
hap = 0 # 각 사이클의 합

while 1:
    cnt += 1 # while문을 돌 때마다 사이클의 길이 1 증가

    hap = mok + rest # 사이클의 합 구하기

    next_num = (rest * 10) + (hap % 10) # 새로운 수

    if num == next_num: # num과 새로운 수가 동일할 경우 while문 탈출
        break

    else: # num과 새로운 수가 동일하지 않을 경우 다음 과정 실행
        mok = next_num // 10
        rest = next_num % 10

print(cnt) # 결과 출력