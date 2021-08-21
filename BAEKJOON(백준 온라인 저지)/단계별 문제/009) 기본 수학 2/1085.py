# 1085번 / 직사각형에서 탈출 / B3
# https://www.acmicpc.net/problem/1085

import math

x, y, w, h = input().split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)

wLength = w-x
hLength = h-y

tup = (x, y, wLength, hLength)

# 최소값을 찾고 최소값을 출력
minValue = min(tup)
print(minValue)
