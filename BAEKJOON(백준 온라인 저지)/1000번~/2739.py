# 2739 / 구구단 / B3
# https://www.acmicpc.net/problem/2739

n = int(input())

for i in range(1, 10) :
    print("{0} * {1} = {2}".format(n, i, n*i))