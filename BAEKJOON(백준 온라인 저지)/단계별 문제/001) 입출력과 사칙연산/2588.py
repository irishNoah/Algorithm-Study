# 2588번 / 곱셈 / B4
# https://www.acmicpc.net/problem/2588

a = int(input())
b = int(input())
c = b

arr = []
for i in range(0, 3) :
    value = b % 10
    arr.append(int(value))
    b = (b - value) / 10


mulValue = []
for i in range(0, 3) :
    value2 = a * arr[i]
    print(value2)

print(a * c)
