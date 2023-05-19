# [백준]1541번-그리디-잃어버린괄호-S2
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/1541

com = input().split('-')

num = []

for operplus in com:
    divPlus = operplus.split('+')

    addResult = 0
    for add in divPlus:
        addResult += int(add)

    num.append(addResult)

result = num[0]

for cnt in range(1, len(num)):
    result -= num[cnt]

print(result)