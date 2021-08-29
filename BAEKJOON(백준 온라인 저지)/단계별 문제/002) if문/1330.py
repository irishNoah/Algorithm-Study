# 1330 / 두 수 비교하기 / B4
# https://www.acmicpc.net/problem/1330

a, b = map(int, input().split())

if a > b :
    print(">")

elif a < b :
    print("<")

else :
    print("==")