# [백준]5585번-그리디-거스름돈-B2
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/5585

coin = [500, 100, 50, 10, 5, 1] # 잔돈 종류

money = int(input()) # 지불할 값 입력
left = 1000 - money # 거스름돈

cnt = 0 # 잔돈의 개수

for i in range(0, 6):
    if (left // coin[i]) > 0:
        mok = left // coin[i]
        cnt += mok

        left = left - (coin[i] * mok)

    # left가 0이 된다면, 더이상 for를 돌 필요가 없음
    if left == 0:
        break

print(cnt)