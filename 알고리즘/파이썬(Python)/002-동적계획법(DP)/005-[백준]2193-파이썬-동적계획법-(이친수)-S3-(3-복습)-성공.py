# [백준]2193-파이썬-동적계획법-(이친수)-S3-(3-복습)-성공.py
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/2193

'''
n = 1부터 5까지 차례대로 이친수를 구했을 때
각 n마다 되는 경우의 수를 구해보면
차례대로 피보나치 값을 형성한다는 것을 알 수 있다.
'''

n = int(input())

if n == 1 or n == 2:
    print(1)

else:
    table = [0] * (n+1)
    table[1] = 1; table[2] = 1

    for i in range(3, n+1):
        table[i] = table[i-1] + table[i-2]

    print(table[n])