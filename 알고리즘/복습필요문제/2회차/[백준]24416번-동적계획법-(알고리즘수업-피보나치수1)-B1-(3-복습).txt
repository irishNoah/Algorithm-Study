# [백준]24416번-동적계획법-(알고리즘수업-피보나치수1)-B1-(3-복습)
# https://github.com/irishNoah/Algorithm-Study
# https://www.acmicpc.net/problem/24416

# 참고 URL > https://jih3508.tistory.com/38

def fib(n):
    global count1
    if n <=2: return 1
    count1 += 1
    return fib(n-1) + fib(n - 2)

def fibonacci(n):
    global count2
    f = [1] * (n + 1)
    for i in range(3, n + 1):
        count2 += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

N = int(input())
count1 = 1
count2 = 0

fib(N)
fibonacci(N)
print(count1, count2)